
from fastapi import FastAPI
from app.routes import zones
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(zones.router, prefix="/zones", tags=["Zones"])
