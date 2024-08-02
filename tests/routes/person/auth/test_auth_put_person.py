import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_person
import os


@pytest.mark.auth
def test_auth_put_person():
    token = get_token_jwt() + "invalid"
    person = create_person()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    person_data_update = {
        "first_name": "editado",
        "last_name": "da silva",
        "birth_date": "25/09/2050"
    }

    client = TestClient(app)
    response = client.put(f"/person/{person['id']}", headers=headers, json=person_data_update)
    assert response.status_code == 200