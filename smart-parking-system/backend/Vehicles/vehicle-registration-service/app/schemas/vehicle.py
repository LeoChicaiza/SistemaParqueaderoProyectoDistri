
from pydantic import BaseModel

class VehicleCreate(BaseModel):
    plate: str
    type: str
    owner: str

class VehicleResponse(BaseModel):
    plate: str
    type: str
    owner: str
