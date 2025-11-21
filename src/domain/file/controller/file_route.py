from fastapi import APIRouter, UploadFile,File, Depends, HTTPException
from sqlalchemy.orm import Session
from common.database import SessionLocal
import os
from domain.file.entity import FileInfo
from common.env import SERVER_URL

router = APIRouter(prefix="/file", tags=["file"])
UPLOAD_FOLDER:str = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload", response_model=FileInfo)
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_name = file.filename
    if file_name is None:
        raise HTTPException(status_code=404, detail="File not found")
    filepath = os.path.join(UPLOAD_FOLDER, file_name)
    with open(filepath, "wb") as f:
        f.write(file.file.read())

    file_info = FileInfo(
        filename=file.filename,
        url=f"{SERVER_URL}/{UPLOAD_FOLDER}/{file.filename}",
        type=file.content_type,
        size=os.path.getsize(filepath),
    )
    db.add(file_info)
    db.commit()
    db.refresh(file_info)
    return file_info
