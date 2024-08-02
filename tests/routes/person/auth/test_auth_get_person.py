import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt


@pytest.mark.auth
def test_auth_get_person():
    token = get_token_jwt() + "invalid"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    client = TestClient(app)
    response = client.get("/person/", headers=headers)
    print(response.json())
    assert response.status_code == 403
