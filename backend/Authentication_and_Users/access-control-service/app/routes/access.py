
from fastapi import APIRouter, HTTPException
from app.schemas.access import RoleAssignment, RoleResponse
from app.database.db import role_db

router = APIRouter()

@router.post("/assign", response_model=RoleResponse)
def assign_role(data: RoleAssignment):
    role_db[data.email] = data.role
    return RoleResponse(email=data.email, role=data.role)

@router.get("/role/{email}", response_model=RoleResponse)
def get_user_role(email: str):
    role = role_db.get(email)
    if not role:
        raise HTTPException(status_code=404, detail="User role not found")
    return RoleResponse(email=email, role=role)
