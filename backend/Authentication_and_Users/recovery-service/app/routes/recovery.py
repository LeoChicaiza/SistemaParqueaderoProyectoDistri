from fastapi import APIRouter, HTTPException
from app.database.db import get_connection

router = APIRouter()

@router.get("/validate-code/{user_id}/{code}")
def validate_recovery_code(user_id: str, code: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM recovery_codes WHERE user_id = %s AND code = %s", (user_id, code))
    valid = cur.fetchone()
    cur.close()
    conn.close()

    if not valid:
        raise HTTPException(status_code=401, detail="Invalid recovery code")
    return {"message": "Recovery code valid"}

