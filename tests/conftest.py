from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, PG_PASS, PG_USER, PG_DB
from server import app
import pytest



DATABASE_URL = f"postgresql://{PG_USER}:{PG_PASS}@172.18.0.2:5432/test_{PG_DB}"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def test_app():
    client = TestClient(app)

    yield client

@pytest.fixture()
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.rollback()
        db.close()