from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from typing import List
from database import get_db
from controller.person_controller import get_all_persons, create_person, get_person, update_person, delete_person
from schema.person_schema import PersonSchema, PersonCreate, PersonUpdate

person_router = APIRouter()

@person_router.get("/", response_model = List[PersonSchema])
def read_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_persons(db, skip=skip, limit=limit)

@person_router.get("/{person_id}", response_model = PersonSchema)
def read_person(person_id: int, db: Session = Depends(get_db)):
    return get_person(db, person_id=person_id)

@person_router.post("/", response_model=PersonSchema)
def create_new_person(person: PersonCreate, db: Session = Depends(get_db)):
    return create_person(db=db, person=person)

@person_router.put("/{person_id}", response_model=PersonSchema)
def update_existing_person(person_id: int, person: PersonUpdate, db: Session = Depends(get_db)):
    return update_person(db=db, person_id=person_id, person=person)

@person_router.delete("/{person_id}")
def delete_existing_person(person_id: int, db: Session = Depends(get_db)):
    delete_person(db=db, person_id=person_id)
    return {"detail": "Person delete"}