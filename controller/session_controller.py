from typing import List
from fastapi import HTTPException, Form
from security import verify_password, create_token_jwt
from sqlalchemy.orm import Session
from model.Session import Sessions
from model.Person import Person
from schema.session_schema import SessionCreate, SessionUpdate
from datetime import datetime


def get_all_sessions(db: Session, skip: int, limit: int) -> List[Session]:
    sessions = db.query(Sessions).offset(skip).limit(limit).all()

    if not sessions:
        raise HTTPException(status_code=404, detail="Not found")
    
    return sessions

def create_session(db: Session, session: SessionCreate) -> Session:
    db_person = db.query(Person).filter(Person.id == session.person_id).first()

    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")


    db_session = Sessions(
        user_agent=session.user_agent,
        ip=session.ip,
        jwt_token=session.jwt_token,
        person_id=session.person_id,
        last_login=datetime.now(),
        end_session=None
    )

    db.add(db_session)
    db.commit()
    db.refresh(db_session)

    return db_session

def get_session(db: Session, session_id: int) -> Session:
    session = db.query(Sessions).filter(Session.id == session_id).first()

    if not session:
        raise HTTPException(status_code=404, detail="Not found")
    
    return session

def update_session(db: Session, session_id: int, session: SessionUpdate) -> Session:
    db_session = db.query(Sessions).filter(Session.id == session_id).first()

    if not db_session:
        raise HTTPException(status_code=404, detail="Not found")
    
    for key, value in session.dict().items():
        setattr(db_session, key, value)

    db.commit()
    db.refresh(db_session)
    return db_session

def delete_session(db: Session, session_id: int) -> dict[str, str]:
    db_session = db.query(Sessions).filter(Session.id == session_id).first()

    if not db_session:
        raise HTTPException(status_code=404, detail="Not found")
    
    db.delete(db_session)
    db.commit()
    return {"message": "Session deleted successfully"}

def login(db: Session, username: str = Form(...), password: str = Form(...)):
    user = db.query(Person).filter(Person.username == username).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": create_token_jwt(user.id),
        "token_type": "Bearer",
        "id_user": user.id
    }