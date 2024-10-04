from pydantic import BaseModel
from datetime import datetime




class SessionResponse(BaseModel):
    id: int
    last_login: datetime
    user_agent: str
    ip: str
    person_id: int

    class Config:
        from_attributes = True
