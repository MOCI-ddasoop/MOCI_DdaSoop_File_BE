from fastapi import UploadFile

from domain.file.dto.ImageFileSizeDTO import ImageFileSizeDTO
from domain.file.entity import FileInfo
from sqlalchemy.orm import Session


class FileRepository:

    async def add_file(
            self,
            db: Session,
            file_name: str,
            url: str,
            type: str | None,
            size: int | None,
            image_file_size: ImageFileSizeDTO
    ) -> FileInfo:
        file_info = FileInfo(
            file_name=file_name,
            url=url,
            type=type,
            size=size,
            width=image_file_size.width,
            height=image_file_size.height
        )
        db.add(file_info)
        db.commit()
        db.refresh(file_info)
        return file_info