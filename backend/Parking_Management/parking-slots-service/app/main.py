
from fastapi import FastAPI
from app.routes import slots
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(slots.router, prefix="/slots", tags=["Parking Slots"])
