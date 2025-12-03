from pydantic import BaseModel, ConfigDict
from datetime import datetime


class FileInfoDTO(BaseModel):
    id: int
    file_name: str
    url: str
    type: str | None
    size: int
    width: int | None
    height: int | None
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)