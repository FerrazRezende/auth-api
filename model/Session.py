from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True, index=True)
    last_login = Column(DateTime, index=True)
    end_session = Column(DateTime, index=True)
    user_agent = Column(String)
    ip = Column(String)
    jwt_token = Column(String)
    person_id = Column(Integer, ForeignKey("person.id"))