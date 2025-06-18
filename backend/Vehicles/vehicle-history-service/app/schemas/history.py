
from pydantic import BaseModel
from typing import List
from datetime import datetime

class HistoryRecord(BaseModel):
    plate: str
    event: str
    timestamp: datetime

class HistoryList(BaseModel):
    records: List[HistoryRecord]
