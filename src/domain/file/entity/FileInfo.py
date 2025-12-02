from sqlalchemy import  Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from common.database import Base

class FileInfo(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String)
    url = Column(String)
    type: str | None = Column(String, nullable=True)
    size: int | None = Column(Integer, nullable=True)
    uploaded_at = Column(DateTime, default=func.now())