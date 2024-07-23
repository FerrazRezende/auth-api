from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from security import get_password_hash

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: str

class PersonCreate(PersonBase):
    pass

class PersonUpdate(BaseModel):
    password: Optional[str] = None

    @validator('password', pre=True)
    def hash_the_password(cls, v):
        if v:
            return get_password_hash(v)
        return v

class PersonSchema(PersonBase):
    id: int
    first_name: str
    last_name: str
    username: str
    created_at: datetime
    last_login: Optional[datetime] = None

    class Config:
        from_attributes = True