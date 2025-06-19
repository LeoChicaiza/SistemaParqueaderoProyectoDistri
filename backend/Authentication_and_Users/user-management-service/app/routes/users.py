from fastapi import APIRouter
from app.database.db import get_connection

router = APIRouter()

@router.post("/create-user")
def create_user(email: str, password: str, role: str = "user"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email, password, role) VALUES (%s, %s, %s)",
                (email, password, role))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "User created successfully"}

