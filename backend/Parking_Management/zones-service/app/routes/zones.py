
from fastapi import APIRouter, HTTPException
from app.schemas.zone import ZoneCreate, ZoneResponse
from app.database.db import zone_db

router = APIRouter()

@router.post("/", response_model=ZoneResponse)
def create_zone(zone: ZoneCreate):
    key = f"{zone.parking_lot}:{zone.level}:{zone.name}"
    if key in zone_db:
        raise HTTPException(status_code=400, detail="Zone already exists")
    zone_db[key] = zone.dict()
    return ZoneResponse(**zone.dict())

@router.get("/{parking_lot}/{level}/{name}", response_model=ZoneResponse)
def get_zone(parking_lot: str, level: int, name: str):
    key = f"{parking_lot}:{level}:{name}"
    zone = zone_db.get(key)
    if not zone:
        raise HTTPException(status_code=404, detail="Zone not found")
    return ZoneResponse(**zone)
