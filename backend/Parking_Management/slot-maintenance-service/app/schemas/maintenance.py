
from pydantic import BaseModel

class MaintenanceRequest(BaseModel):
    parking_lot: str
    level: int
    zone: str
    slot_id: str

class MaintenanceStatus(BaseModel):
    slot_id: str
    status: str
