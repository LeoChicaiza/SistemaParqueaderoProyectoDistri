
from pydantic import BaseModel

class ZoneCreate(BaseModel):
    parking_lot: str
    level: int
    name: str
    type: str  # ejemplo: 'General', 'Discapacitados', 'VIP'

class ZoneResponse(BaseModel):
    parking_lot: str
    level: int
    name: str
    type: str
