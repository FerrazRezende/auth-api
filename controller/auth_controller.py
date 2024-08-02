from fastapi import HTTPException, Form, Request
from security import verify_password, create_token_jwt, get_password_hash, generate_random_code
from sqlalchemy.orm import Session
from model.Session import Sessions
from model.Person import Person
from datetime import datetime




def login(request: Request, db: Session, username: str = Form(...), password: str = Form(...)):
    user = db.query(Person).filter(Person.username == username).first()
    print(user)
    

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token_jwt(user.id)
    
    session_data = Sessions(
        user_agent=request.headers.get("user-agent"),
        ip=request.client.host,
        jwt_token=token,
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


def change_user_password(request: Request, db: Session, username: str, new_password: str, reset_code: str):
    db_person = db.query(Person).filter(Person.username == username).first()
    generated_code = "1234"
    print(f"code {generated_code}")

    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")

    if reset_code != generated_code:
        raise HTTPException(status_code=401, detail="Invalid reset code")

    if new_password is not None:
        db_person.password = get_password_hash(new_password)


    db.commit()
    db.refresh(db_person)
    return {"message": "Password updated successfully"}