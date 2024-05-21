from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from contextlib import contextmanager

import os 

load_dotenv()

PG_PASS = os.getenv("PG_PASS")
PG_USER = os.getenv("PG_USER")
PG_DB = os.getenv("PG_DB")


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    
    finally:
        db.close()


DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASS}@localhost:5432/{PG_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()