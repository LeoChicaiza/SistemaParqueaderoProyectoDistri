
from fastapi import FastAPI
from app.routes import recovery
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(recovery.router, prefix="/recovery", tags=["Password Recovery"])
