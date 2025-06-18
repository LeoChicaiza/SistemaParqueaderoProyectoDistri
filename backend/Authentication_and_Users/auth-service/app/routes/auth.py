
from fastapi import APIRouter, HTTPException
from app.schemas.user import UserLogin, TokenResponse
from app.utils.jwt_handler import create_jwt_token

router = APIRouter()

# Simulando una "base de datos" temporal
fake_users_db = {
    "admin@example.com": {
        "password": "admin123",  # en la práctica deberías usar hashes
        "role": "admin"
    }
}

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    db_user = fake_users_db.get(user.email)
    if not db_user or db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_jwt_token({"email": user.email, "role": db_user["role"]})
    return TokenResponse(access_token=token)
