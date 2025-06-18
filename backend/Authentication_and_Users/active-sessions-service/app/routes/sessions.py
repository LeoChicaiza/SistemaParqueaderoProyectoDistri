
from fastapi import APIRouter, HTTPException
from app.schemas.session import SessionData, SessionResponse
from app.database.db import sessions_db

router = APIRouter()

@router.post("/start", response_model=SessionResponse)
def start_session(data: SessionData):
    sessions_db[data.email] = data.token
    return SessionResponse(email=data.email, status="Session started")

@router.delete("/end/{email}", response_model=SessionResponse)
def end_session(email: str):
    if email not in sessions_db:
        raise HTTPException(status_code=404, detail="Session not found")
    del sessions_db[email]
    return SessionResponse(email=email, status="Session ended")

@router.get("/active/{email}", response_model=SessionResponse)
def get_session(email: str):
    token = sessions_db.get(email)
    if not token:
        raise HTTPException(status_code=404, detail="Session not found")
    return SessionResponse(email=email, status="Active")
