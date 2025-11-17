from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.common.database import Base

class FileInfo(Base):
    __tablename__ = "file_info"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)


