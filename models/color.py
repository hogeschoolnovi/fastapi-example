from sqlalchemy import Column, Integer, String
from .base import Base

class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
