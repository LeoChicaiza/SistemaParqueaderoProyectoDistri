
from fastapi import FastAPI
from app.routes import registration
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(registration.router, prefix="/vehicles", tags=["Vehicle Registration"])
