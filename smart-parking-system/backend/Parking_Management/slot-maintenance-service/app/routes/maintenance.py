
from fastapi import APIRouter, HTTPException
from app.schemas.maintenance import MaintenanceRequest, MaintenanceStatus
from app.database.db import maintenance_db

router = APIRouter()

@router.post("/mark", response_model=MaintenanceStatus)
def mark_slot_for_maintenance(data: MaintenanceRequest):
    key = f"{data.parking_lot}:{data.level}:{data.zone}:{data.slot_id}"
    maintenance_db[key] = "maintenance"
    return MaintenanceStatus(slot_id=data.slot_id, status="maintenance")

@router.post("/release", response_model=MaintenanceStatus)
def release_slot_from_maintenance(data: MaintenanceRequest):
    key = f"{data.parking_lot}:{data.level}:{data.zone}:{data.slot_id}"
    if key not in maintenance_db:
        raise HTTPException(status_code=404, detail="Slot not under maintenance")
    del maintenance_db[key]
    return MaintenanceStatus(slot_id=data.slot_id, status="available")

@router.get("/status/{parking_lot}/{level}/{zone}/{slot_id}", response_model=MaintenanceStatus)
def check_slot_status(parking_lot: str, level: int, zone: str, slot_id: str):
    key = f"{parking_lot}:{level}:{zone}:{slot_id}"
    status = "maintenance" if key in maintenance_db else "available"
    return MaintenanceStatus(slot_id=slot_id, status=status)
