import pytest
import os
from fastapi.testclient import TestClient
from server import app

@pytest.mark.route
def test_create_person(db_session):
    token = os.getenv('CREATE_TOKEN')
    headers = {
        "token": f"{token}"
    }

    person_data = {
      "first_name": "teste",
      "last_name": "porra",
      "birth_date": "01/05/2055",
      "username": "teste.porra",
      "password": "testehehe"
    }

    client = TestClient(app)
    response = client.post("/person/", json=person_data, headers=headers)

    assert response.status_code == 200