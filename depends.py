from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from schema.session_schema import TokenPayload

from model.Person import Person
from security import JWT_SECRET_KEY, JWT_ALGORITHM

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/session/login")


def get_current_user(token: str = Depends(reusable_oauth2), db: Session = Depends(get_db)) -> Person:
    try: 
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        token_data = TokenPayload(**payload)
    
    except (jwt.JWTError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token inválido")
    
    user = db.query(Person).filter(Person.id == token_data.sub).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    
    return user