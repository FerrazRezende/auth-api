from typing import List, Type
from fastapi import HTTPException
from sqlalchemy.orm import Session
from model.Session import Sessions




# Function for list all sessions
def get_all_sessions(db: Session, skip: int, limit: int) -> List[Type[Sessions]]:
    sessions = db.query(Sessions).offset(skip).limit(limit).all()

    if not sessions:
        raise HTTPException(status_code=404, detail="Not found")
    
    return sessions

# Function to get specific session without their session id
def get_session(db: Session, session_id: int) -> Type[Sessions]:
    session = db.query(Sessions).filter(Sessions.id == session_id).first()

    if not session:
        raise HTTPException(status_code=404, detail="Not found")
    
    return session
