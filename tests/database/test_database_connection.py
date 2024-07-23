import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

def test_database_connection(db_session):
    try:
        result = db_session.execute(text("SELECT 1"))

        assert result is not None, "The query returned None"

    except SQLAlchemyError as e:
        pytest.fail(f"Database connection failed: {e}")