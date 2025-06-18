
from fastapi import FastAPI
from app.routes import control
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(control.router, prefix="/control", tags=["Access Control"])
