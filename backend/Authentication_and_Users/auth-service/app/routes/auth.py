from fastapi import APIRouter, HTTPException
from app.schemas.user import UserLogin, TokenResponse
from app.utils.jwt_handler import create_jwt_token
from app.database.db import get_connection

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT password, role FROM users WHERE email = %s", (user.email,))
    db_user = cur.fetchone()
    cur.close()
    conn.close()

    if not db_user or db_user[0] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_jwt_token({"email": user.email, "role": db_user[1]})
    return TokenResponse(access_token=token)
