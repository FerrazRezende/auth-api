from fastapi import HTTPException, APIRouter, Depends, Header
from sqlalchemy.orm import Session 
from typing import List, Optional, Union
from database import get_db
from controller.person_controller import get_all_persons, create_person, get_person, update_person, delete_person, get_person_by_criteria
from schema.person_schema import PersonCreate, PersonUpdate, PersonQueryParams
from responses.person_response import PersonResponse, PersonUpdateResponse
from depends import get_current_user
import os


person_router = APIRouter()


@person_router.get("/search", response_model=Union[PersonResponse, List[PersonResponse]], dependencies=[Depends(get_current_user)])
async def search_persons(query_params: PersonQueryParams = Depends(), db: Session = Depends(get_db)):
    return get_person_by_criteria(db, 
                                  first_name=query_params.first_name, 
                                  last_name=query_params.last_name, 
                                  username=query_params.username
                                  )

@person_router.get("/", response_model = List[PersonResponse], dependencies=[Depends(get_current_user)])
async def read_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_persons(db, skip=skip, limit=limit)

@person_router.get("/{person_id}", response_model = PersonResponse, dependencies=[Depends(get_current_user)])
async def read_person(person_id: int, db: Session = Depends(get_db)):
    return get_person(db, person_id=person_id)

@person_router.post("/", response_model=PersonResponse)
async def create_new_person(person: PersonCreate, token: str = Header(...), db: Session = Depends(get_db)):
    if token != os.getenv("CREATE_TOKEN"):
        raise HTTPException(status_code=403, detail="Forbidden")

    with db as session:
        return create_person(db=session, person=person)

@person_router.put("/{person_id}", response_model=PersonUpdateResponse, dependencies=[Depends(get_current_user)])
async def update_existing_person(person_id: int, person: PersonUpdate, db: Session = Depends(get_db)):
    return update_person(db=db, person_id=person_id, person=person)

@person_router.delete("/{person_id}", dependencies=[Depends(get_current_user)])
async def delete_existing_person(person_id: int, db: Session = Depends(get_db)):
    delete_person(db=db, person_id=person_id)
    return {"detail": "Person delete"}


