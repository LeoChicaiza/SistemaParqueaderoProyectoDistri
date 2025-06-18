
from fastapi import FastAPI
from app.routes import history
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(history.router, prefix="/history", tags=["Vehicle History"])
