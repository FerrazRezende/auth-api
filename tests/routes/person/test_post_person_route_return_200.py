import requests
import requests_mock
import json
from datetime import datetime


def crate_person(person_data):
    response = requests.post("http://localhost:8000/person/", json=person_data)
    return response


def test_create_person():
    person_data = {
        "first_name": "Matheus",
        "last_name": "Ferraz",
        "birth_date": "15/09/2000"
    }

    with requests_mock.Mocker() as m:
        m.post("http://localhost:8000/person/", status_code=200)
        response = crate_person(person_data)
        assert response.status_code == 200