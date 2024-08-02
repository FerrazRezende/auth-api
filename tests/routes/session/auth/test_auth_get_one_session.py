import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_session


@pytest.mark.auth
def test_get_one_session():
    token = get_token_jwt()

    session = create_session(token)

    headers = {
        "Authorization": f"Bearer {token} invalid"
    }

    client = TestClient(app)
    response = client.get(f"/session/{session['id']}", headers=headers)

    assert response.status_code == 403