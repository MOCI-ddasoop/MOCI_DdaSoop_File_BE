from fastapi import UploadFile
from sqlalchemy.orm import Session
import os
from PIL import ImageFile

from domain.file.dto.ImageFileSizeDTO import ImageFileSizeDTO


class FileService:

    def __init__(self):
        os.makedirs('./uploads', exist_ok=True)

    async def upload(
            self, file: UploadFile
    ):
        target_dir = "./uploads"
        os.makedirs(target_dir, exist_ok=True)
        key = file.filename
        tmp_path = os.path.join(target_dir, f".tmp_{key}")
        final_path = os.path.join(target_dir, key)
        with open(tmp_path, "wb") as f:
            while chunk := await file.read(1048576):
                f.write(chunk)

        os.replace(tmp_path, final_path)

