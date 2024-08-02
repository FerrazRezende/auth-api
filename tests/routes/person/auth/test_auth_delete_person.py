import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_person


@pytest.mark.auth
def test_auth_delete_person():
    invalid_token = get_token_jwt() + "invalid"
    person = create_person()

    headers = {
        "Authorization": f"Bearer {invalid_token}"
    }
    
    client = TestClient(app)
    response = client.delete(f"/person/{person['id']}", headers=headers)
    assert response.status_code == 403