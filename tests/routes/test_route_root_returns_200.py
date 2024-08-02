from fastapi.testclient import TestClient
from server import app

def test_route_root_returns_200():
    test_app = TestClient(app)
    response = test_app.get("/")
    assert response.status_code == 200