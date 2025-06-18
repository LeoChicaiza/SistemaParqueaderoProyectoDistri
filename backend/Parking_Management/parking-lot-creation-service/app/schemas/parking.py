
from pydantic import BaseModel

class ParkingLotCreate(BaseModel):
    name: str
    address: str
    capacity: int

class ParkingLotResponse(BaseModel):
    name: str
    address: str
    capacity: int
