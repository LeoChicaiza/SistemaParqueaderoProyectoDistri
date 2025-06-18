
from fastapi import APIRouter, HTTPException
from app.schemas.level import LevelCreate, LevelResponse
from app.database.db import level_db

router = APIRouter()

@router.post("/", response_model=LevelResponse)
def create_level(level: LevelCreate):
    key = f"{level.parking_lot}:{level.level_number}"
    if key in level_db:
        raise HTTPException(status_code=400, detail="Level already exists")
    level_db[key] = level.dict()
    return LevelResponse(**level.dict())

@router.get("/{parking_lot}/{level_number}", response_model=LevelResponse)
def get_level(parking_lot: str, level_number: int):
    key = f"{parking_lot}:{level_number}"
    level = level_db.get(key)
    if not level:
        raise HTTPException(status_code=404, detail="Level not found")
    return LevelResponse(**level)
