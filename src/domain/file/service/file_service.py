from fastapi import UploadFile
from sqlalchemy.orm import Session
import os
from PIL import ImageFile

from common.env import settings
from domain.file.dto.ImageFileSizeDTO import ImageFileSizeDTO
from domain.file.entity import FileInfo
from domain.file.repository import FileRepository


class FileService:

    def __init__(self, repository: FileRepository):
        os.makedirs(settings.FILE_ROOT_PATH, exist_ok=True)
        self.repo = repository

    async def upload(
            self, file: UploadFile,
            key:str, subdir: str | None = None
    ) -> ImageFileSizeDTO:
        target_dir = os.path.join(settings.FILE_ROOT_PATH, subdir or "")
        os.makedirs(target_dir, exist_ok=True)

        tmp_path = os.path.join(target_dir, f".tmp_{key}")
        final_path = os.path.join(target_dir, key)
        parser = ImageFile.Parser()
        width:int | None = None
        height:int | None = None
        with open(tmp_path, "wb") as f:
            while chunk := await file.read(settings.FILE_BUFFER_SIZE):
                f.write(chunk)

                parser.feed(chunk)
                if parser.image:
                    width, height = parser.image.size

        os.replace(tmp_path, final_path)
        return ImageFileSizeDTO(
            width=width,
            height=height,
        )

    async def add_file(self, file: UploadFile,db:Session, key: str, image_file_size:ImageFileSizeDTO) -> FileInfo:
        url = os.path.join(settings.SERVER_URL, key)
        return await self.repo.add_file(
            db=db,
            file_name=key,
            url=url,
            type=file.content_type,
            size=file.size,
            image_file_size=image_file_size
        )
