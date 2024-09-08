import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_person


@pytest.mark.person
def test_delete_person():
    token = get_token_jwt(
        "matheus",
        "ferraz",
        "15/09/2000",
        "matheus.ferraz1",
        "12345678"
    )
    person = create_person(
        "teste",
        "almeida",
        "15/09/2000",
        "teste.almeida1",
        "12345678"
    )

    print(person, token)

    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    client = TestClient(app)
    response = client.delete(f"/person/{person['id']}", headers=headers)
    assert response.status_code == 200