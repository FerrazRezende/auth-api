import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_person

@pytest.mark.auth
def test_auth_get_one_person():
    token = get_token_jwt() + 'invalid'
    person = create_person()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    client = TestClient(app)
    response = client.get(f"/person/{person['id']}", headers=headers)
    assert response.status_code == 403