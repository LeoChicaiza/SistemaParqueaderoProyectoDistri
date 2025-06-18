
from fastapi import FastAPI
from app.routes import parking
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(parking.router, prefix="/parking-lots", tags=["Parking Lots"])
