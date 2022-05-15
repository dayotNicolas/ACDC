from fastapi.testclient import TestClient
import app

client = TestClient(app)

def test_main():
    response = client.get('/')
    assert response.status_code == 200

def test_region():
    response = client.get('/regions/')
    assert response.status_code == 200

def test_hospitalisation():
    response = client.get('/hospitalisation/')
    assert response.status_code == 200

def test_death():
    response = client.get('/death/')
    assert response.status_code == 200

def test_vaccinPercentage():
    response = client.get('/vaccinPercentage/')
    assert response.status_code == 200