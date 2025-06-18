
from fastapi import APIRouter, HTTPException
from app.schemas.vehicle import VehicleCreate, VehicleResponse
from app.database.db import vehicle_db

router = APIRouter()

@router.post("/", response_model=VehicleResponse)
def register_vehicle(vehicle: VehicleCreate):
    if vehicle.plate in vehicle_db:
        raise HTTPException(status_code=400, detail="Vehicle already registered")
    vehicle_db[vehicle.plate] = vehicle.dict()
    return VehicleResponse(**vehicle.dict())

@router.get("/{plate}", response_model=VehicleResponse)
def get_vehicle(plate: str):
    vehicle = vehicle_db.get(plate)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return VehicleResponse(**vehicle)
