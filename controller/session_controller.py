from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from model.Session import Sessions




def get_all_sessions(db: Session, skip: int, limit: int) -> List[Session]:
    sessions = db.query(Sessions).offset(skip).limit(limit).all()

    if not sessions:
        raise HTTPException(status_code=404, detail="Not found")
    
    return sessions

def get_session(db: Session, session_id: int) -> Session:
    session = db.query(Sessions).filter(Sessions.id == session_id).first()

    if not session:
        raise HTTPException(status_code=404, detail="Not found")
    
    return session
