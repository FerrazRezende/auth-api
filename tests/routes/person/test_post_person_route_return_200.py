import pytest
import os
from fastapi.testclient import TestClient
from server import app

@pytest.mark.route
def test_create_person(db_session):
    token = os.getenv('CREATE_TOKEN')
    headers = {
        "Authorization": f"{token}"
    }

    person_data = {
        "first_name": "teste",
        "last_name": "da silva",
        "birth_date": "15/09/2000"
    }

    client = TestClient(app)
    response = client.post("/person/", json=person_data, headers=headers)
    assert response.status_code == 200