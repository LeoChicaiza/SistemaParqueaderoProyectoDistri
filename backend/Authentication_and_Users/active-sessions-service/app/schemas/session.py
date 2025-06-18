
from pydantic import BaseModel

class SessionData(BaseModel):
    email: str
    token: str

class SessionResponse(BaseModel):
    email: str
    status: str
