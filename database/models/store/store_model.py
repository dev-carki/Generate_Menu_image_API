# app/models.py
from sqlalchemy import Column, Integer, String, Time, DateTime, func, text
from sqlalchemy.sql import expression
from database.database import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
    open_time = Column(Time, nullable=True)
    close_time = Column(Time, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
