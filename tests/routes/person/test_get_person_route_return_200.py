# from tests.conftest import test_app
# import requests
# import pytest

# def get_jwt_token():
#     url = "http://localhost:8000/session/login"
#     credential = {
#         "username": "teste.date",
#         "password": "Levi2021@"
#     }

#     response = requests.post(url, data=credential)
#     print(response.json())
#     return response.json()["access_token"]

# @pytest.mark.route
# def test_get_person_route_return_200(test_app):
#     token = get_jwt_token()

#     headers = {
#         "Authorization": f"Bearer {token}"
#     }

#     response = test_app.get("/person/1", headers=headers)
#     assert response.status_code == 200