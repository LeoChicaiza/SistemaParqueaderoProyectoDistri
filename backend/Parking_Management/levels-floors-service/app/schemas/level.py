
from pydantic import BaseModel

class LevelCreate(BaseModel):
    parking_lot: str
    level_number: int
    description: str

class LevelResponse(BaseModel):
    parking_lot: str
    level_number: int
    description: str
