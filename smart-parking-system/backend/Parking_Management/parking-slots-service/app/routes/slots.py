
from fastapi import APIRouter, HTTPException
from app.schemas.slot import SlotCreate, SlotResponse
from app.database.db import slot_db

router = APIRouter()

@router.post("/", response_model=SlotResponse)
def create_slot(slot: SlotCreate):
    key = f"{slot.parking_lot}:{slot.level}:{slot.zone}:{slot.slot_id}"
    if key in slot_db:
        raise HTTPException(status_code=400, detail="Slot already exists")
    slot_db[key] = slot.dict()
    return SlotResponse(**slot.dict())

@router.get("/{parking_lot}/{level}/{zone}/{slot_id}", response_model=SlotResponse)
def get_slot(parking_lot: str, level: int, zone: str, slot_id: str):
    key = f"{parking_lot}:{level}:{zone}:{slot_id}"
    slot = slot_db.get(key)
    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")
    return SlotResponse(**slot)
