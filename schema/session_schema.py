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
    last_login: Optional[datetime] = None

class SessionSchema(SessionBase):
    id: int
    last_login: datetime
    end_session: Optional[datetime] = None  # new line

    class Config:
        orm_mod = True


class TokenPayload(BaseModel):
    sub: Optional[int] = None

class TokenData(BaseModel):
    access_token: str
    token_type: str