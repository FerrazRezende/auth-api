# from tests.conftest import test_app
# import requests
# import pytest
#
# def get_jwt_token():
#     url = "http://localhost:8000/session/login"
#
#     credentials = {
#         "username": "teste.date",
#         "password": "Levi2021@"
#     }
#
#     response = requests.post(url, data=credentials)
#     return response.json()['access_token']
#
#
# def test_update_person(test_app):
#     token = get_jwt_token()
#
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#
#     update_person_data = {
#         "first_name": ""
#     }