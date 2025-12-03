from pydantic import BaseModel


class ImageFileSizeDTO(BaseModel):
    width: int | None
    height: int | None
