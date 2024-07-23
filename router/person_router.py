from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from typing import List
from database import get_db
from controller.person_controller import get_all_persons, create_person, get_person, update_person, delete_person
from schema.person_schema import PersonCreate, PersonUpdate
from responses.person_response import PersonResponse, PersonUpdateResponse
<<<<<<< HEAD
from depends import get_current_user
=======
from depends import get_current_user, verify_create_token
>>>>>>> 6ccfcf3 (getting started with automated testing)

person_router = APIRouter()


@person_router.get("/", response_model = List[PersonResponse], dependencies=[Depends(get_current_user)])
def read_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_persons(db, skip=skip, limit=limit)

@person_router.get("/{person_id}", response_model = PersonResponse, dependencies=[Depends(get_current_user)])
def read_person(person_id: int, db: Session = Depends(get_db)):
    return get_person(db, person_id=person_id)

<<<<<<< HEAD
@person_router.post("/", response_model=PersonResponse, dependencies=[Depends(get_current_user)])
=======
@person_router.post("/", response_model=PersonResponse, dependencies=[Depends(verify_create_token)])
>>>>>>> 6ccfcf3 (getting started with automated testing)
def create_new_person(person: PersonCreate, db: Session = Depends(get_db)):
    with db as session:
        return create_person(db=session, person=person)

<<<<<<< HEAD
@person_router.put("/{person_id}", response_model=PersonUpdateResponse, dependencies=[Depends(get_current_user)])
=======
@person_router.put("/{person_id}", response_model=PersonUpdateResponse)
>>>>>>> 6ccfcf3 (getting started with automated testing)
def update_existing_person(person_id: int, person: PersonUpdate, db: Session = Depends(get_db)):
    return update_person(db=db, person_id=person_id, person=person)

@person_router.delete("/{person_id}", dependencies=[Depends(get_current_user)])
def delete_existing_person(person_id: int, db: Session = Depends(get_db)):
    delete_person(db=db, person_id=person_id)
    return {"detail": "Person delete"}
