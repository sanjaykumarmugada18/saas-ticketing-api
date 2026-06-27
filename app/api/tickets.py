from fastapi import APIRouter, Depends, status, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db, SessionLocal
from app.models.user import User
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketResponse, TicketUpdate
from app.api.deps import get_current_user, get_current_active_agent
from app.services.ai_service import analyze_ticket_text

router = APIRouter(prefix="/tickets", tags=["Tickets"])


# -----------------------------
# Background Worker
# -----------------------------
async def process_ticket_with_ai(
    ticket_id: int,
    title: str,
    description: str,
):
    # Ask the AI to analyze the ticket
    ai_result = await analyze_ticket_text(title, description)

    # Open a fresh database session
    db = SessionLocal()

    try:
        # Fetch the latest ticket using the fresh session
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

        if ticket:
            ticket.category = ai_result.get(
                "category",
                "Uncategorized"
            )

            ticket.priority = ai_result.get(
                "priority",
                "Low"
            )

            db.commit()
            db.refresh(ticket)

    except Exception as e:
        print(f"Background Task Database Error: {e}")

    finally:
        db.close()


# -----------------------------
# Create Ticket
# -----------------------------
@router.post("/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def create_ticket(
    ticket: TicketCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        owner_id=current_user.id
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    # Fire-and-Forget AI processing
    background_tasks.add_task(
        process_ticket_with_ai,
        ticket_id=new_ticket.id,
        title=new_ticket.title,
        description=new_ticket.description,
    )

    return new_ticket


# -----------------------------
# Read Tickets
# -----------------------------
@router.get("/", response_model=List[TicketResponse])
def read_tickets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role in ["agent", "admin"]:
        tickets = (
            db.query(Ticket)
            .offset(skip)
            .limit(limit)
            .all()
        )
    else:
        tickets = (
            db.query(Ticket)
            .filter(Ticket.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    return tickets


# -----------------------------
# Update Ticket Status
# -----------------------------
@router.patch("/{ticket_id}", response_model=TicketResponse)
def update_ticket_status(
    ticket_id: int,
    update_data: TicketUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_agent),
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    ticket.status = update_data.status

    db.commit()
    db.refresh(ticket)

    return ticket