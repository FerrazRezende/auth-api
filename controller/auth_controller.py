from security import verify_password, create_token_jwt, get_password_hash
from fastapi import HTTPException, Form, Request, File
from settings import REDIS_CLIENT, EXPIRATION_TIME
from schema.auth_schema import ChangePass
from sqlalchemy.orm import Session
from model.Session import Sessions
from model.Person import Person
from typing import Dict, Type
from datetime import datetime
from utils import save_image
from mail import send_email
import random




# |-----------------|
# | Auth Controller |
# |-----------------|
# Function responsible for all api login logic
def login(
        request: Request,
        db: Session,
        username: str = Form(...),
        password: str = Form(...)
) -> Dict[str, str | int]:

    user = db.query(Person).filter(Person.username == username).first()
    print(user)
    

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token_jwt(user.id)

    session_data = Sessions(
        user_agent=request.headers.get("user-agent"),
        ip=request.client.host,
        person_id=user.id,
        last_login=datetime.now(),
    )

    db.add(session_data)
    db.commit()
    db.refresh(session_data)

    return {
        "access_token": token,
        "token_type": "Bearer",
        "id_user": user.id
    }

# Function responsible for changing the user's password using the random code generated in another function
def change_user_password(payload: ChangePass, db: Session) -> Dict[str, str]:
    db_person = db.query(Person).filter(Person.username == payload.username).first()

    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")

    stored_reset_code = REDIS_CLIENT.get(f"reset_code: {payload.username}")

    if stored_reset_code is None or stored_reset_code != payload.reset_code:
        raise HTTPException(status_code=400, detail="Reset code invalid")


    if payload.new_password is not None:
        db_person.password = get_password_hash(payload.new_password)

    db.commit()
    db.refresh(db_person)

    REDIS_CLIENT.delete(f"reset_code:{payload.username}")
    return {"message": "Password updated successfully"}

# Function responsible for sending the reset code to the user's email so that they can reset their password
def get_reset_code(username: str, request: Request, db: Session) -> Dict[str, str]:
    reset_code = random.randint(100000, 999999)
    person = db.query(Person).filter(Person.username == username).first()

    REDIS_CLIENT.setex(f"reset_code: {username}", EXPIRATION_TIME, reset_code)

    send_email(person.email, str(reset_code))

    return {"message": f"Reset code generated successfully and send to email: {person.email}"}

# Function responsible for checking that the token is still valid and has not expired
def verify_token(current_user: Person) -> Dict[str, str | int]:
    return {"status": "Token is valid", "person_id": current_user.id}

# Function to send the user's photo
def upload_user_photo(
        file: Type[File],
        current_user: Person
) -> Dict[str, str]:
    username = current_user.username

    try:
        file_path = save_image(file, username)

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error saving file")

    return {"message": f"File uploaded successfully", "filepath": file_path}