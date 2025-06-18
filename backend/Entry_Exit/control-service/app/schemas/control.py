
from pydantic import BaseModel
from datetime import datetime

class AccessLog(BaseModel):
    plate: str
    direction: str  # 'entry' o 'exit'
    timestamp: datetime

class AccessResponse(BaseModel):
    message: str
