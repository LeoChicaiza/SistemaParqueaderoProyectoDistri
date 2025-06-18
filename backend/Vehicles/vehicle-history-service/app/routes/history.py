
from fastapi import APIRouter, HTTPException
from app.schemas.history import HistoryRecord, HistoryQuery, HistoryList
from app.database.db import history_db

router = APIRouter()

@router.post("/add", response_model=HistoryRecord)
def add_history(record: HistoryRecord):
    history_db.setdefault(record.plate, []).append(record.dict())
    return record

@router.get("/{plate}", response_model=HistoryList)
def get_history(plate: str):
    if plate not in history_db:
        raise HTTPException(status_code=404, detail="No history found for this plate")
    return HistoryList(records=history_db[plate])
