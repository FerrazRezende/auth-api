from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from model.Person import Person
from schema.person_schema import PersonCreate, PersonUpdate


def get_all_persons(db: Session, skip: int, limit: int) -> List[Person]:
    person = db.query(Person).offset(skip).limit(limit).all()

    if not person:
        raise HTTPException(status_code=404, details="Not found")
    
    return person

def create_person(db: Session, person: PersonCreate) -> Person:
    db_person = Person(
        first_name=person.first_name,
        last_name=person.last_name,
        birth_date=person.last_name,
        username=f"{person.first_name}.{person.last_name}",
        password="123"
    )

    db.add(db_person)
    db.commit()
    db.refresh(db_person)

    return db_person

def get_person(db: Session, person_id: int) -> Person:
    person = db.query(Person).filter(Person.id == person_id).first()

    if not person:
        raise HTTPException(status_code=404, details="Not found")
    
    return person

def update_person(db: Session, person_id: int, person: PersonUpdate) -> Person:
    db_person = db.query(Person).filter(Person.id == person_id).first()

    if not db_person:
        raise HTTPException(status_code=404, details="Not found")
    
    for key, value in person.dict().items():
        setattr(db_person, key, value)

    db.commit()
    db.refresh(db_person)
    return db_person

def delete_person(db: Session, person_id: int) -> Person:
    db_person = db.query(Person).filter(Person.id == person_id)

    if not db_person:
        raise HTTPException(status_code=404, details="Not found")
    
    db.delete(db_person)
    db.commit()
    return {"message": "Person deleted successfully"}