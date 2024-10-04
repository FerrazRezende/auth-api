from pydantic import BaseModel, validator
from datetime import datetime, date




class PersonResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    birth_date: str
    username: str
    created_at: str

    @validator('birth_date', 'created_at', pre=True)
    def convert_dates(cls, v) -> str:
        if isinstance(v, (datetime, date)):
            return v.isoformat()
        return v

    class Config:
        from_attributes = True