from urllib import response
import pytest
from fastapi.testclient import TestClient

import app

client = TestClient(app)

@pytest.mark.skip()
def test_main():
    response = client.get('/')
    #assert response.status_code_code == 200
    print(response.json())

test_main()