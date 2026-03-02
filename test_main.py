from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Asalamualeykum"}

def test_sum():
    response = client.get("/sum?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}
    
def_multiply():
    response = client.get("/multiply?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 35}