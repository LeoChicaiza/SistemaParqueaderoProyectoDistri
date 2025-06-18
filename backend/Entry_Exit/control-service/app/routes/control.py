
from fastapi import APIRouter, HTTPException
from app.schemas.control import AccessLog, AccessResponse
from app.database.db import access_log

router = APIRouter()

@router.post("/", response_model=AccessResponse)
def log_access(data: AccessLog):
    key = f"{data.plate}-{data.timestamp}"
    access_log[key] = data.dict()
    return AccessResponse(message="Access logged successfully")

@router.get("/{plate}", response_model=list[AccessLog])
def get_access_logs(plate: str):
    logs = [log for key, log in access_log.items() if log['plate'] == plate]
    if not logs:
        raise HTTPException(status_code=404, detail="No access logs found")
    return logs
