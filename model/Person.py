from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func
from database import Base

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    password = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    birth_date = Column(Date)
    created_at = Column(DateTime, server_default=func.now())
