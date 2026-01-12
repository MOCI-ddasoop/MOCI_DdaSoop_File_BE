from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
import os

from domain.file.dto.FileInfoDTO import FileInfoDTO
from dependency_injector.wiring import inject, Provide
from domain.file.service import FileService
from common.dependency_injector import Container
import asyncio
from pathlib import Path
import uuid

router = APIRouter(prefix="/file", tags=["file"])
UPLOAD_FOLDER:str = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/url")
async def create_upload_url():
    return {"file_url":f"http://localhost:8000/file"}

@router.get("/url")
async def get_file_url(
        file_name:str = Query(description="File URL"),
):
    if not os.path.exists(f"uploads/{file_name}"):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")
    return {"file_url" : f"http://localhost:8000/uploads/{file_name}"}

@router.post("/")
@inject
async def upload_file(
        file: UploadFile = File(...),
        svc: FileService = Depends(Provide[Container.file_service])
):
    await svc.upload(file)

@router.delete("/{file_name}")
async def delete_file(
        file_name:str,
):
    target_dir = "./uploads"
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, file_name)
    if os.path.exists(target_path):
        os.remove(target_path)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")



