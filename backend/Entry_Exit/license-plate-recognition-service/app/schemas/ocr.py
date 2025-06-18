
from pydantic import BaseModel

class OCRResponse(BaseModel):
    plate: str
    confidence: float
