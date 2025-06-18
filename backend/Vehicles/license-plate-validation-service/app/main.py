
from fastapi import FastAPI
from app.routes import validation

app = FastAPI()

app.include_router(validation.router, prefix="/plate-validation", tags=["Plate Validation"])
