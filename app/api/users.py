from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import get_password_hash

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Hash the password
    hashed_pw = get_password_hash(user.password)

    # 3. Create the SQLAlchemy model instance
    new_user = User(email=user.email, hashed_password=hashed_pw)

    #4. Save to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user