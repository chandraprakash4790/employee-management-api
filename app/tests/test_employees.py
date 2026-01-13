from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    return client.post("/api/token").json()["access_token"]

def test_create_employee():
    token = get_token()
    res = client.post("/api/employees/", headers={"Authorization": f"Bearer {token}"},
                      json={"name": "Vishal", "email": "vishal@test.com"})
    assert res.status_code == 201
