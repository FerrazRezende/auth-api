from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional
import bleach

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    birth_date: str
    username: str
    password: str


    @validator('birth_date', pre=True)
    def validate_birth_date(cls, v) -> Optional[str]:
        try:
            return datetime.strptime(v, '%d/%m/%Y').strftime('%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be DD/MM/YYYY")

    @validator('first_name', pre=True)
    def validate_first_name(cls, v) -> Optional[str]:
        try:
            return v.capitalize()
        except ValueError:
            pass

    @validator('last_name', pre=True)
    def validate_last_name(cls, v) -> Optional[str]:
        try:
            return v.capitalize()
        except ValueError:
            pass

class PersonCreate(PersonBase):
    pass

class PersonUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None

    @validator('first_name', 'last_name', pre=True)
    def validate_first_name(cls, v) -> Optional[str]:
        try:
            return v.capitalize()
        except ValueError:
            pass


class PersonSchema(PersonBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class PersonQueryParams(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    username: Optional[str] = Field(None, max_length=50)

    @validator('first_name', 'last_name', 'username', pre=True, always=True)
    def sanitize_strings(cls, v) -> Optional[str]:
        if v is not None:
            return bleach.clean(v)
        return v