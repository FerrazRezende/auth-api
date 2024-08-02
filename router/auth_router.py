from fastapi import APIRouter, Depends, Form, Request
from sqlalchemy.orm import Session 
from database import get_db
from controller.auth_controller import login, change_user_password
from schema.auth_schema import TokenData

auth_router = APIRouter()


@auth_router.post("/login", response_model=TokenData)
def login_user(request: Request, db: Session = Depends(get_db), username: str = Form(...), password: str = Form(...)):
    return login(request, db, username, password)


@auth_router.put("/change_password")
def change_password(request: Request, db: Session = Depends(get_db), username: str = Form(...), new_password: str = Form(...), reset_code: str = Form(...)):   
    return change_user_password(request, db, username, new_password, reset_code)