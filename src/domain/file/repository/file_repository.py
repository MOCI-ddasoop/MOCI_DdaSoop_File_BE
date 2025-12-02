from fastapi import UploadFile
from domain.file.entity import FileInfo
from sqlalchemy.orm import Session


class FileRepository:

    async def add_file(
            self,
            db: Session,
            filename,
            url,
            type,
            size
    ) -> FileInfo:
        file_info = FileInfo(
            filename=filename,
            url=url,
            type=type,
            size=size,
        )
        db.add(file_info)
        db.commit()
        db.refresh(file_info)
        return file_info