from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from security import get_password_hash
import bleach

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    username: str
    password: str


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
    birth_date: Optional[datetime] = None
    username: Optional[str] = None
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

class PersonQueryParams(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    username: Optional[str] = Field(None, max_length=50)

    @validator('first_name', 'last_name', 'username', pre=True, always=True)
    def sanitize_strings(cls, v):
        if v is not None:
            return bleach.clean(v)
        return v