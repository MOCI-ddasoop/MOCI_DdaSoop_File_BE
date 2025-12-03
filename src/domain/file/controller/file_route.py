from fastapi import APIRouter, UploadFile,File, Depends, HTTPException
from sqlalchemy.orm import Session
import os

from domain.file.dto.FileInfoDTO import FileInfoDTO
from common.database import SessionLocal
from dependency_injector.wiring import inject, Provide
from domain.file.service import FileService
from common.dependency_injector import Container
from common.env import settings
from domain.file.entity import FileInfo
import asyncio
from pathlib import Path
import uuid

router = APIRouter(prefix="/file", tags=["file"])
UPLOAD_FOLDER:str = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload", response_model=FileInfoDTO)
@inject
async def upload_file(
        file: UploadFile = File(...),
        db: Session = Depends(get_db),
        svc: FileService = Depends(Provide[Container.file_service])
) -> FileInfo:
    ext = Path(file.filename).suffix if file.filename else ""
    key = f"{uuid.uuid4().hex}{ext}"
    image_file_size = await svc.upload(file, key)
    return await svc.add_file(file, db, key, image_file_size)


