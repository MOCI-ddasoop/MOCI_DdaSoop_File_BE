from pydantic import BaseModel
from datetime import datetime

class FileInfo(BaseModel):
    id: int
    filename: str
    url: str
    type: str | None
    size: int | None
    uploaded_at: datetime

    class Config:
        orm_mode = True



