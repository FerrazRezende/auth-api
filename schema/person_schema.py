from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from security import get_password_hash

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: str

    @validator('birth_date', pre=True)
    def validate_birth_date(cls, v):
        try:
            return datetime.strptime(v, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be DD/MM/YYYY")

class PersonCreate(PersonBase):
    pass

class PersonUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[str] = None
    password: Optional[str] = None

    @validator('password', pre=True)
    def hash_the_password(cls, v):
        if v:
            return get_password_hash(v)
        return v

    @validator('birth_date', pre=True)
    def validate_birth_date(cls, v):
        if v:
            try:
                return datetime.strptime(v, '%d/%m/%Y').strftime('%Y-%m-%d')
            except ValueError:
                raise ValueError("Incorrect date format, should be DD/MM/YYYY")
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