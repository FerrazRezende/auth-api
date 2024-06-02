from pydantic import BaseModel


class PersonResponse(BaseModel):
    id: int
    first_name: str
    birth_date: str
    username: str
    created_at: str

    class Config:
        orm_mode = True

class PersonUpdateResponse(BaseModel):
    id: int
    username: str