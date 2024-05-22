from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

import os 

load_dotenv()

PG_PASS = os.getenv("PG_PASS")
PG_USER = os.getenv("PG_USER")
PG_DB = os.getenv("PG_DB")

DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASS}@localhost:5432/{PG_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    
    finally:
        db.close()


Base = declarative_base()
metadata = MetaData()