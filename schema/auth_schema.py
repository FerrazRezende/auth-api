from pydantic import BaseModel
from typing import Optional

class TokenPayload(BaseModel):
    sub: Optional[int] = None

class TokenData(BaseModel):
    access_token: str
    token_type: str
    id_user: int

class ChangePass(BaseModel):
    username: str
    new_password: str
    reset_code: str