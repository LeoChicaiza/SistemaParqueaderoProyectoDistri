
from fastapi import FastAPI
from app.routes import availability
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(availability.router, prefix="/availability", tags=["Availability"])
