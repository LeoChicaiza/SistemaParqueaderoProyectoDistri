
from pydantic import BaseModel

class RecoveryRequest(BaseModel):
    email: str

class RecoveryResponse(BaseModel):
    email: str
    message: str
