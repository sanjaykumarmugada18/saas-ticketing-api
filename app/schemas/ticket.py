from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.ticket import TicketStatus

# 1. Shared properties (Keeps our code DRY)
class TicketBase(BaseModel):
    title: str
    description: str

# 2. Properties to receive on ticket creation
class TicketCreate(TicketBase):
    pass # 'pass' means it just inherits the base fields and adds nothing else

# 3. Properties to return to the client
class TicketResponse(TicketBase):
    id: int
    status: TicketStatus

    category: str
    priority: str

    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

class TicketUpdate(BaseModel):
    status: TicketStatus