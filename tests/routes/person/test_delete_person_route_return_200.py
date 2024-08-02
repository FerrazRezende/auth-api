import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_person


@pytest.mark.route
def test_delete_person():
    token = get_token_jwt()
    person = create_person()

    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    client = TestClient(app)
    response = client.delete(f"/person/{person['id']}", headers=headers)
    assert response.status_code == 200