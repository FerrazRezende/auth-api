from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: str

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    username: Optional[str] = None
    password: Optional[str] = None

class PersonSchema(PersonBase):
    id: int
    first_name: str
    last_name: str
    username: str
    created_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        orm_mode = True