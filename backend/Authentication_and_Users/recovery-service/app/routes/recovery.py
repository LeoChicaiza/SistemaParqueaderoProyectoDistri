
from fastapi import APIRouter, HTTPException
from app.schemas.recovery import RecoveryRequest, RecoveryResponse
from app.database.db import user_passwords

router = APIRouter()

@router.post("/", response_model=RecoveryResponse)
def recover_password(request: RecoveryRequest):
    if request.email not in user_passwords:
        raise HTTPException(status_code=404, detail="User not found")
    # Simulación de envío de correo (no real)
    return RecoveryResponse(email=request.email, message="Recovery email sent")
