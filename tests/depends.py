from fastapi.testclient import TestClient
from server import app
from datetime import datetime
from security import get_password_hash
import os

def get_token_jwt(first_name, last_name, birth_date, username, password):
    person_r = create_person(first_name, last_name, birth_date, username, password)

    client = TestClient(app)

    login_data = {
        "username": person_r['user'],
        "password": person_r['pass'],
    }

    r = client.post("/auth/login/", data=login_data)

    print(login_data)

    return r.json()['access_token']

def create_person(first_name, last_name, birth_date, username, password):
    token = os.getenv("CREATE_TOKEN")

    headers = {
        "token": token
    }

    person_data = {
      "first_name": first_name,
      "last_name": last_name,
      "birth_date": birth_date,
      "username": username,
      "password": password
    }

    client = TestClient(app)
    response = client.post("/person/", headers=headers, json=person_data)

    return {
        "id": response.json()['id'],
        "user": response.json()['username'],
        "pass": person_data['password']
    }


def create_session(token):
    person = create_person()

    session_data = {
        "last_login": datetime.now().isoformat(),
        "user_agent": "Mozilla/5.0",
        "ip": "192.168.1.1",
        "jwt_token": "token",
        "attemps": 1,
        "person_id": person['id']
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    client = TestClient(app)
    response = client.post("/session/", headers=headers, json=session_data)

    return response.json()
