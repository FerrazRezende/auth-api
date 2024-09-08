from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from settings import DATABASE_URL

# Vars for setting db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Function to create db session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    
    finally:
        db.close()


Base = declarative_base()
metadata = MetaData()