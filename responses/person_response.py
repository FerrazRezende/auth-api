from pydantic import BaseModel


class PersonResponse(BaseModel):
    id: int
    first_name: str
    birth_date: str
    username: str
    created_at: str

    class Config:
<<<<<<< HEAD
        orm_mode = True
=======
        from_attributes = True
>>>>>>> 6ccfcf3 (getting started with automated testing)

class PersonUpdateResponse(BaseModel):
    id: int
    username: str