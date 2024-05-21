from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from schema.person_schema import PersonBase
from datetime import datetime
from database import Base

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    password = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    birth_date = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    last_login = Column(DateTime)
