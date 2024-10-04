from controller.session_controller import get_all_sessions, get_session
from responses.session_response import SessionResponse
from fastapi import APIRouter, Depends
from depends import get_current_user
from sqlalchemy.orm import Session
from database import get_db
from typing import List



# Router instance /session/
session_router = APIRouter()

# /session/
@session_router.get(
    "/",
    response_model = List[SessionResponse],
    dependencies=[Depends(get_current_user)]
)
async def read_sessions(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
) -> List[Session]:

    """
    Read all sessions
    """

    return get_all_sessions(db, skip=skip, limit=limit)

# /session/{session_id}
@session_router.get(
    "/{session_id}",
    response_model = SessionResponse,
    dependencies=[Depends(get_current_user)]
)
async def read_session(session_id: int, db: Session = Depends(get_db)) -> Session:

    """
    Read specific session with an session id
    """

    return get_session(db, session_id=session_id)


