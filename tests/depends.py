from fastapi.testclient import TestClient
from server import app
from datetime import datetime
import os

def get_token_jwt():
    client = TestClient(app)

    token = os.getenv('CREATE_TOKEN')
    headers = {
        "token": f"{token}"
    }

    person_data = {
        "first_name": "matheus",
        "last_name": "ferraz",
        "birth_date": "15/09/2000"
    }

    r = client.post("/person/", json=person_data, headers=headers)

    person_r = r.json()

    password = "123456"
    password_data = {
        "password": password
    }

    client.put(f"/person/{person_r['id']}", json=password_data)

    login_data = {
        "username": person_r['username'],
        "password": password
    }

    r = client.post("/session/login/", data=login_data)

    return r.json()['access_token']

def create_person():
    token = os.getenv("CREATE_TOKEN")

    headers = {
        "token": token
    }

    person_data = {
        "first_name": "teste",
        "last_name": "da silva",
        "birth_date": "25/09/2050"
    }

    client = TestClient(app)
    response = client.post("/person/", headers=headers, json=person_data)

    return response.json()

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
