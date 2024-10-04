import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import PG_PASS, PG_USER, TEST_PG_DB
from server import app
from database import get_db

Base = declarative_base()

@pytest.fixture(scope="session")
def test_engine():
        return create_engine(f"postgresql://{PG_USER}:{PG_PASS}@172.27.0.2:5432/{TEST_PG_DB}")

@pytest.fixture(scope="session")
def TestSessionLocal(test_engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="session", autouse=True)
def setup_database(test_engine):
    Base.metadata.create_all(bind=test_engine)

    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def db_session(TestSessionLocal):
    db = TestSessionLocal()
    
    try:
        yield db

    finally:
        db.rollback()
        db.close()

@pytest.fixture(scope="function", autouse=True)
def override_get_db(db_session):
    app.dependency_overrides[get_db] = lambda: db_session

    yield
    app.dependency_overrides[get_db] = get_db

def clean_db_with_sql(db_session):

    tables_to_clean = ['person', 'session']

    for table in tables_to_clean:
        result = db_session.execute(text(f"SELECT * FROM {table}"))
        exists = result.scalar()

        if exists:
            print(f"Delete data from {table}")
            db_session.execute(text(f"DELETE FROM {table}"))
        
        else:
            print(f"table {table} is empty")

    db_session.commit()

    print("Database cleaned")    


@pytest.fixture(scope="function", autouse=True)
def clean_database(db_session):
    clean_db_with_sql(db_session)