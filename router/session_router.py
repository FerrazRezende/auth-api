from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from typing import List
from database import get_db
from controller.session_controller import get_all_sessions, get_session
from responses.session_response import SessionResponse
from depends import get_current_user

session_router = APIRouter()



@session_router.get("/", response_model = List[SessionResponse], dependencies=[Depends(get_current_user)])
async def read_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_sessions(db, skip=skip, limit=limit)

@session_router.get("/{session_id}", response_model = SessionResponse, dependencies=[Depends(get_current_user)])
async def read_session(session_id: int, db: Session = Depends(get_db)):
    return get_session(db, session_id=session_id)


