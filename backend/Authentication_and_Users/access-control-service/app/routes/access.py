from fastapi import APIRouter, HTTPException
from app.database.db import get_connection

router = APIRouter()

@router.get("/permissions/{user_id}")
def get_user_permissions(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT permission FROM permissions WHERE user_id = %s", (user_id,))
    permissions = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()

    if not permissions:
        raise HTTPException(status_code=404, detail="Permissions not found")
    return {"permissions": permissions}

