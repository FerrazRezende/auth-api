import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_session
from datetime import datetime


@pytest.mark.auth
def test_auth_put_session():
    token = get_token_jwt()

    session = create_session(token)

    headers = {
        "Authorization": f"Bearer {token} invalid"
    }

    session_data_update = {
        "person_id": session['person_id'],
        "last_login": datetime.now().isoformat(),
        "user_agent": "Edge/5.0",
        "ip": "172.0.18.1",
        "jwt_token": "token",
        "attemps": 3,
    }

    client = TestClient(app)
    response = client.put(f"/session/{session['id']}", headers=headers, json=session_data_update)
    print(response.json())
    assert response.status_code == 403