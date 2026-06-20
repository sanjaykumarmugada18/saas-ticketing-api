from pydantic import BaseModel, EmailStr, ConfigDict

# Schema for incoming data(Registration)
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schema for outgoing data (Returning user details)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    model_config = ConfigDict(from_attributes=True)