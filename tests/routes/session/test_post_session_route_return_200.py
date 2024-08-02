import pytest
from fastapi.testclient import TestClient
from server import app
from tests.depends import get_token_jwt, create_person
from datetime import datetime

@pytest.mark.route
def test_create_session(db_session):
    token = get_token_jwt()
    person = create_person()

    headers = {
        "Authorization": f"Bearer {token}"
    } 

    session_data = {
        "last_login": datetime.now().isoformat(),
        "user_agent": "Mozilla/5.0",
        "ip": "192.168.1.1",
        "jwt_token": "token",
        "attemps": 1,
        "person_id": person['id']
    }

    client = TestClient(app)
    response = client.post("/session/", headers=headers, json=session_data)
    
    assert response.status_code == 200