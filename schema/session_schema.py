from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SessionBase(BaseModel):
    user_agent: str
    ip: str
    jwt_token: str
    person_id: int

class SessionCreate(SessionBase):
    pass

class SessionUpdate(SessionBase):
    person_id: Optional[int]
    user_agent: Optional[str] = None
    ip: Optional[str] = None
    jwt_token: Optional[str] = None
    last_login: Optional[datetime] = None

class SessionSchema(SessionBase):
    id: int
    last_login: datetime

    class Config:
        from_attributes = True

