
from fastapi import FastAPI
from app.routes import users
from app.database import db

app = FastAPI()

@app.on_event("startup")
def startup():
    db.init()

app.include_router(users.router, prefix="/users", tags=["Users"])
