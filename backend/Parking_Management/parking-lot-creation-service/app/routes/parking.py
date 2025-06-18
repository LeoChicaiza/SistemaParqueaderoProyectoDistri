
from fastapi import APIRouter, HTTPException
from app.schemas.parking import ParkingLotCreate, ParkingLotResponse
from app.database.db import parking_db

router = APIRouter()

@router.post("/", response_model=ParkingLotResponse)
def create_parking_lot(parking: ParkingLotCreate):
    if parking.name in parking_db:
        raise HTTPException(status_code=400, detail="Parking lot already exists")
    parking_db[parking.name] = parking.dict()
    return ParkingLotResponse(**parking.dict())

@router.get("/{name}", response_model=ParkingLotResponse)
def get_parking_lot(name: str):
    lot = parking_db.get(name)
    if not lot:
        raise HTTPException(status_code=404, detail="Parking lot not found")
    return ParkingLotResponse(**lot)
