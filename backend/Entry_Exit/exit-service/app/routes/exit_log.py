
from fastapi import APIRouter, HTTPException
from app.schemas.exit import ExitRequest, ExitResponse
from app.database.db import exit_records

router = APIRouter()

@router.post("/", response_model=ExitResponse)
def register_exit(data: ExitRequest):
    if data.plate in exit_records:
        raise HTTPException(status_code=400, detail="Vehicle already exited")
    exit_records[data.plate] = data.timestamp
    return ExitResponse(plate=data.plate, exit_time=data.timestamp)

@router.get("/{plate}", response_model=ExitResponse)
def get_exit(plate: str):
    if plate not in exit_records:
        raise HTTPException(status_code=404, detail="No exit record found")
    return ExitResponse(plate=plate, exit_time=exit_records[plate])
