from passlib.context import CryptContext
from typing import Any, Union
from datetime import datetime, timedelta
from jose import jwt
import os



JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_EXPIRATION_TIME_MINUTES = int(os.getenv('JWT_EXPIRATION_TIME_MINUTES'))

<<<<<<< HEAD
=======
CREATE_TOKEN = os.getenv('CREATE_TOKEN')

>>>>>>> 6ccfcf3 (getting started with automated testing)

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def create_token_jwt(subject: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)