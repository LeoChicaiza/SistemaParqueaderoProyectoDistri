from fastapi import APIRouter
from app.database.db import get_connection

router = APIRouter()

@router.get("/sessions/{user_id}")
def get_active_sessions(user_id: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT session_id, created_at FROM active_sessions WHERE user_id = %s", (user_id,))
    sessions = [{"session_id": row[0], "created_at": row[1]} for row in cur.fetchall()]
    cur.close()
    conn.close()
    return {"active_sessions": sessions}

