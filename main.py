from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Asalamualeykum"}

@app.get('/sum')
def get_sum(a: int, b: int):
    return {"result": a + b}

def test_sum():
    response = client.get("/sum?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}
    
def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    
def test_divide():
    response = client.get("/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}