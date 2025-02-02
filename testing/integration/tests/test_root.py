"""
Only one test in here..
Runs first and it is to check the ROOT of the API
"""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.order("first")
def test_root_path(client: TestClient):
    """
    Testing root
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.is_success
    assert response.reason_phrase == "OK"
    assert response.request.method == "GET"
    assert response.json() == {"msg": "Hello World!"}
