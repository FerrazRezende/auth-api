from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from typing import List
from database import get_db
from controller.session_controller import get_all_sessions, create_session, get_session, update_session, delete_session
from schema.session_schema import SessionSchema, SessionCreate, SessionUpdate

session_router = APIRouter()



@session_router.get("/", response_model = List[SessionSchema])
def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_sessions(db, skip=skip, limit=limit)

@session_router.get("/{session_id}", response_model = SessionSchema)
def read_session(session_id: int, db: Session = Depends(get_db)):
    return get_session(db, session_id=session_id)

@session_router.post("/", response_model=SessionSchema)
def create_new_session(session_: SessionCreate, db: Session = Depends(get_db)):
    with db as session:
        return create_session(db=session, session=session_)

@session_router.put("/{session_id}", response_model=SessionSchema)
def update_existing_session(session_id: int, session: SessionUpdate, db: Session = Depends(get_db)):
    return update_session(db=db, session_id=session_id, session=session)

@session_router.delete("/{session_id}")
def delete_existing_session(session_id: int, db: Session = Depends(get_db)):
    delete_session(db=db, session_id=session_id)
    return {"detail": "Session delete"}