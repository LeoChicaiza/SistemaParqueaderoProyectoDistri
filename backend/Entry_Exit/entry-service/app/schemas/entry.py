
from pydantic import BaseModel
from datetime import datetime

class EntryRequest(BaseModel):
    plate: str
    timestamp: datetime

class EntryResponse(BaseModel):
    plate: str
    entry_time: datetime
