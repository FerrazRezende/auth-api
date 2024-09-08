import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_person



@pytest.mark.route
def test_get_person():
    token = get_token_jwt(
        "matheus",
        "ferraz",
        "15/09/2000",
        "matheus.ferraz3",
        "12345678"
    )
    person = create_person(
        "teste",
        "almeida",
        "15/09/2000",
        "teste.almeida2",
        "12345678"
    )

    headers = {
        "Authorization": f"Bearer {token}"
    }

    person_data_update = {
        "first_name": "editado",
        "last_name": "almeida",
        "birth_date": "25/09/2050"
    }

    client = TestClient(app)
    response = client.put(f"/person/{person['id']}", headers=headers, json=person_data_update)
    assert response.status_code == 200