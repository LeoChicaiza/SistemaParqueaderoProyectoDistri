
from fastapi import FastAPI
from app.routes import exit_log
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(exit_log.router, prefix="/exit", tags=["Vehicle Exit"])
