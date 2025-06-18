
from pydantic import BaseModel

class PlateRequest(BaseModel):
    plate: str

class PlateResponse(BaseModel):
    plate: str
    valid: bool
