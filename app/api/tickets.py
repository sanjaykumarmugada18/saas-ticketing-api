from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketResponse
from app.api.deps import get_current_user

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Construct the database object securely
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        owner_id=current_user.id  # The ultimate defense against BOLA
    )
    
    # Save to PostgreSQL
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    
    return new_ticket