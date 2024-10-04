from schema.person_schema import PersonCreate, PersonUpdate
from typing import List, Type, Optional, Union, Dict
from security import get_password_hash
from model.Session import Sessions
from sqlalchemy.orm import Session
from fastapi import HTTPException
from model.Person import Person
from datetime import datetime
from sqlalchemy import or_




# |-------------------|
# | Person Controller |
# |-------------------|
# Function for list all persons
def get_all_persons(db: Session, skip: int, limit: int) -> List[Type[Person]]:
    persons = db.query(Person).offset(skip).limit(limit).all()

    if not persons:
        raise HTTPException(status_code=404, detail="Not found")
    
    for person in persons:
        person.birth_date = person.birth_date.isoformat()
        person.created_at = person.created_at.isoformat()
    
    return persons

# Function for create person with 'CREATE TOKEN'
def create_person(db: Session, person: PersonCreate) -> Person:
    birth_date = datetime.strptime(person.birth_date, '%Y-%m-%d').date()

    hashed_password = get_password_hash(person.password)

    db_person = Person(
        first_name=person.first_name,
        last_name=person.last_name,
        email=person.email,
        birth_date=birth_date,
        username=person.username.lower(),
        password=hashed_password
    )

    db.add(db_person)
    db.commit()
    db.refresh(db_person)

    db_person.birth_date = db_person.birth_date.isoformat()
    db_person.created_at = db_person.created_at.isoformat()

    return db_person

# Function for get specific person with their id
def get_person(db: Session, person_id: int) -> Type[Person]:
    person = db.query(Person).filter(Person.id == person_id).first()

    if not person:
        raise HTTPException(status_code=404, detail="Not found")
    
    person.created_at = person.created_at.isoformat()
    person.birth_date = person.birth_date.isoformat()

    return person

# Function to edit a person using their id
def update_person(db: Session, person_id: int, person: PersonUpdate) -> Type[Person]:
    db_person = db.query(Person).filter(Person.id == person_id).first()

    if not db_person:
        raise HTTPException(status_code=404, detail="Person not found")
    
    for key, value in vars(person).items():
        if value is not None:
            setattr(db_person, key, value)

    db.commit()
    db.refresh(db_person)
    return db_person

# Function to remove a person using their id
def delete_person(db: Session, person_id: int) -> Dict[str, str]:
    db_sessions = db.query(Sessions).filter(Sessions.person_id == person_id).all()
    for session in db_sessions:
        db.delete(session)

    db_person = db.query(Person).filter(Person.id == person_id).first()
    if not db_person:
        raise HTTPException(status_code=404, detail="Not found")
    
    db.delete(db_person)
    db.commit()
    return {"message": "Person deleted successfully"}

# Search an user using first name, last name or username
def get_person_by_criteria(
        db: Session,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        username: Optional[str] = None
) -> Union[Person, List[Type[Person]], Type[Person]]:

    person = None

    if first_name:
        first_name = first_name.capitalize()

    if last_name:
        last_name = last_name.capitalize()

    if first_name and last_name:
        person = db.query(Person).filter(Person.first_name == first_name, Person.last_name == last_name).first()

    elif first_name or last_name:
        persons = db.query(Person).filter(or_(Person.first_name == first_name, Person.last_name == last_name)).all()

        for p in persons:
            p.birth_date = p.birth_date.isoformat()
            p.created_at = p.created_at.isoformat()

        if len(persons) == 1:
            return persons[0]

        if len(persons) == 0:
            raise HTTPException(status_code=404, detail="Not found")

        return persons
    
    elif username:
        person = db.query(Person).filter(Person.username == username).first()

    if not person:
        raise HTTPException(status_code=404, detail="Not found")
    
    person.birth_date = person.birth_date.isoformat()
    person.created_at = person.created_at.isoformat()

    return person
    