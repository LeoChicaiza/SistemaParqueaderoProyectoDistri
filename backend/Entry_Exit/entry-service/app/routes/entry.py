
from fastapi import APIRouter, HTTPException
from app.schemas.entry import EntryRequest, EntryResponse
from app.database.db import entry_log

router = APIRouter()

@router.post("/", response_model=EntryResponse)
def register_entry(data: EntryRequest):
    if data.plate in entry_log:
        raise HTTPException(status_code=400, detail="Vehicle already entered")
    entry_log[data.plate] = data.timestamp
    return EntryResponse(plate=data.plate, entry_time=data.timestamp)

@router.get("/{plate}", response_model=EntryResponse)
def get_entry(plate: str):
    if plate not in entry_log:
        raise HTTPException(status_code=404, detail="No entry record found")
    return EntryResponse(plate=plate, entry_time=entry_log[plate])
