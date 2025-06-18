
from fastapi import APIRouter
from app.schemas.availability import SlotAvailability, AvailabilityResponse
from app.database.db import slot_status_db

router = APIRouter()

@router.post("/update", response_model=AvailabilityResponse)
def update_availability(status: SlotAvailability):
    key = f"{status.parking_lot}:{status.level}:{status.zone}:{status.slot_id}"
    slot_status_db[key] = status.status
    return AvailabilityResponse(slot_id=status.slot_id, status=status.status)

@router.get("/{parking_lot}/{level}/{zone}", response_model=list[AvailabilityResponse])
def get_availability(parking_lot: str, level: int, zone: str):
    results = []
    for key, value in slot_status_db.items():
        p, l, z, s = key.split(":")
        if p == parking_lot and int(l) == level and z == zone:
            results.append(AvailabilityResponse(slot_id=s, status=value))
    return results
