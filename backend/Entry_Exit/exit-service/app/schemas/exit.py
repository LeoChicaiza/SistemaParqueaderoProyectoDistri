
from pydantic import BaseModel
from datetime import datetime

class ExitRequest(BaseModel):
    plate: str
    timestamp: datetime

class ExitResponse(BaseModel):
    plate: str
    exit_time: datetime
