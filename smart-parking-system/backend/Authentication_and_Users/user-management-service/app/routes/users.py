
from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse
from app.database.db import users_db

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.email] = {
        "name": user.name,
        "email": user.email,
        "password": user.password
    }
    return UserResponse(name=user.name, email=user.email)
