
from fastapi import FastAPI
from app.routes import levels
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(levels.router, prefix="/levels", tags=["Levels and Floors"])
