from pydantic import BaseModel, ConfigDict
from datetime import datetime


class FileInfoDTO(BaseModel):
    id: int
    filename: str
    url: str
    type: str | None
    size: int
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)