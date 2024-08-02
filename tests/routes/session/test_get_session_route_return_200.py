import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_session

@pytest.mark.route
def test_get_session():
    token = get_token_jwt()

    create_session(token)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    client = TestClient(app)
    response = client.get("/session/", headers=headers)
    print(response.json())
    assert response.status_code == 200