
from fastapi import APIRouter, HTTPException
from app.schemas.plate import PlateRequest, PlateResponse
import re

router = APIRouter()

PLATE_REGEX = r"^[A-Z]{3}-\d{3,4}$"

@router.post("/", response_model=PlateResponse)
def validate_plate(data: PlateRequest):
    if not re.match(PLATE_REGEX, data.plate):
        raise HTTPException(status_code=400, detail="Invalid plate format")
    return PlateResponse(plate=data.plate, valid=True)
