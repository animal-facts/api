"""
Conftest file for fixtures.
"""

import os
from typing import Iterator

import pytest
from httpx import Client

WEB_ENV = os.getenv("WEB", "http://0.0.0.0:8080")


@pytest.fixture(scope="session")
def client() -> Iterator[Client]:
    """
    Return the TestClient
    """
    with Client(base_url=WEB_ENV) as _client:
        try:
            yield _client
        finally:
            _client.close()
