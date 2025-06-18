
from pydantic import BaseModel

class RoleAssignment(BaseModel):
    email: str
    role: str

class RoleResponse(BaseModel):
    email: str
    role: str
