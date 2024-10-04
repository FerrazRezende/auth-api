from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from security import JWT_SECRET_KEY, JWT_ALGORITHM
from schema.auth_schema import TokenPayload
from sqlalchemy.orm import Session
from model.Person import Person
from database import get_db
from typing import Type
from jose import jwt




# Login route
reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

# |-------------------|
# | Depends functions |
# |-------------------|
def get_current_user(token: str = Depends(reusable_oauth2), db: Session = Depends(get_db)) -> Type[Person]:
    try: 
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        token_data = TokenPayload(**payload)
    
    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")
    
    user = db.query(Person).filter(Person.id == token_data.sub).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user