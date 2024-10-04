from fastapi import APIRouter, Depends, Form, Request, UploadFile, File
from schema.auth_schema import TokenData, ChangePass
from depends import get_current_user
from sqlalchemy.orm import Session
from typing import Dict, Annotated
from model.Person import Person
from database import get_db
from controller.auth_controller import (
    login,
    change_user_password,
    get_reset_code,
    verify_token,
    upload_user_photo
)




# Router instance /auth/
auth_router = APIRouter()

# /auth/login/
@auth_router.post("/login", response_model=TokenData)
def login_user(
        request: Request,
        db: Session = Depends(get_db),
        username: str = Form(...),
        password: str = Form(...)
):
    """
    To log in to the application

    receives username + password and returns TokenJWT, token type and user ID
    """
    return login(request, db, username, password)

# /auth/change_password/
@auth_router.put("/change_password")
def change_password(request: Request,  payload: ChangePass,  db: Session = Depends(get_db)):
    """
    For reset password

    This endpoint recive reset code generated in 'reset_code' endpoint
    """
    return change_user_password(request, payload, db)

# /auth/new_reset_code/
"""
Send reset code in user email
"""
@auth_router.get("/new_reset_code")
async def reset_code(username: str, request: Request, db: Session = Depends(get_db)):
    return get_reset_code(username, request, db)

# /auth/verify/
@auth_router.get("/verify")
def verify(current_user: Person = Depends(get_current_user)) -> Dict[str, str | int]:
    """
    Check that the token is still valid and has not expired
    """
    return verify_token(current_user)

# auth/upload_photo/
@auth_router.post("/upload_photo/")
def send_photo(
        file: Annotated[UploadFile, File(description="User profile image")],
        current_user: Person = Depends(get_current_user)
) -> Dict[str, str]:
    """
    Send the user's photo and if there is no folder named with the user's username, the folder will be created.
    """
    return upload_user_photo(file, current_user)
