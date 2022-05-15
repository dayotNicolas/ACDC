import pytest
from fastapi.testclient import TestClient
from urllib import response

from project_ACDC.app import app
from project_ACDC.add_function import add

@pytest.mark.skip()
def test_add():
    assert add(3, 5) == 8

client = TestClient(app)

@pytest.mark.skip()
def test_main():
    response = client.get('/')
    #assert response.status_code_code == 200
    print(response.json())
