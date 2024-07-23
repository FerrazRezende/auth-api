from tests.conftest import test_app

def test_route_root_returns_200(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}