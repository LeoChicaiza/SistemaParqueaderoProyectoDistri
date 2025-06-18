
from pydantic import BaseModel

class SlotCreate(BaseModel):
    parking_lot: str
    level: int
    zone: str
    slot_id: str
    status: str  # ejemplo: 'available', 'occupied', 'maintenance'

class SlotResponse(BaseModel):
    parking_lot: str
    level: int
    zone: str
    slot_id: str
    status: str
