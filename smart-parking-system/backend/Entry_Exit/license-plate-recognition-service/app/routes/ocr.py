
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.ocr import OCRResponse

router = APIRouter()

@router.post("/recognize", response_model=OCRResponse)
async def recognize_plate(file: UploadFile = File(...)):
    # Simulación: Devuelve una placa ficticia
    if not file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        raise HTTPException(status_code=400, detail="Invalid image format")
    return OCRResponse(plate="ABC-1234", confidence=0.97)
