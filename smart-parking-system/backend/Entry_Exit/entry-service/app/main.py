
from fastapi import FastAPI
from app.routes import entry
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(entry.router, prefix="/entry", tags=["Vehicle Entry"])
