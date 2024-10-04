from schema.person_schema import PersonCreate, PersonUpdate, PersonQueryParams
from fastapi import HTTPException, APIRouter, Depends, Header, Response
from responses.person_response import PersonResponse
from depends import get_current_user
from sqlalchemy.orm import Session
from typing import List, Union
from database import get_db
import os
from controller.person_controller import (
    get_all_persons,
    create_person,
    get_person,
    update_person,
    delete_person,
    get_person_by_criteria
)




# Router instance /person/
person_router = APIRouter()

# /person/search?{prop}=
@person_router.get(
    "/search",
    response_model=Union[PersonResponse, List[PersonResponse]],
    dependencies=[Depends(get_current_user)]
)
async def search_persons(query_params: PersonQueryParams = Depends(), db: Session = Depends(get_db)):

    """
    Search an user using first name, last name or username
    """

    return get_person_by_criteria(
        db,
        first_name=query_params.first_name,
        last_name=query_params.last_name,
        username=query_params.username
    )

@person_router.get("/", response_model = List[PersonResponse], dependencies=[Depends(get_current_user)])
async def read_persons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    """
    Get all persons
    """

    return get_all_persons(db, skip=skip, limit=limit)

@person_router.get("/{person_id}", response_model = PersonResponse, dependencies=[Depends(get_current_user)])
async def read_person(person_id: int, response: Response, db: Session = Depends(get_db)):

    """
    Get specific person with an person id
    """

    return get_person(db, person_id=person_id)

@person_router.post("/", response_model=PersonResponse)
async def create_new_person(person: PersonCreate, token: str = Header(...), db: Session = Depends(get_db)):

    """
    Create person with 'CREATE_TOKEN'
    """

    if token != os.getenv("CREATE_TOKEN"):
        raise HTTPException(status_code=403, detail="Forbidden")

    with db as session:
        return create_person(db=session, person=person)

@person_router.put("/{person_id}", response_model=PersonResponse, dependencies=[Depends(get_current_user)])
async def update_existing_person(person_id: int, person: PersonUpdate, db: Session = Depends(get_db)):
    """
    Update a person's data with that person's ID
    """

    return update_person(db=db, person_id=person_id, person=person)

@person_router.delete("/{person_id}", dependencies=[Depends(get_current_user)])
async def delete_existing_person(person_id: int, db: Session = Depends(get_db)):

    """
    Delete a person with their id
    """

    delete_person(db=db, person_id=person_id)
    return {"detail": "Person delete"}


