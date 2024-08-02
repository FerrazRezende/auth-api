import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt


@pytest.mark.route
def test_get_person():
    token = get_token_jwt()
    headers = {
        "Authorization": f"Bearer {token}"
    }

    client = TestClient(app)
    response = client.get("/person/", headers=headers)
    assert response.status_code == 200
