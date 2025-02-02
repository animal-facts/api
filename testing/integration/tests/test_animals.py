"""
Testing module for animal fact endpoints.
"""

from uuid import uuid4

import httpx
import pytest

from testing.integration.schemas import Animal

BASE_ENDPOINT = "/facts/"
QUERY_ANIMAL = "animal"
ANIMAL_TYPES = ["bird", "dog", "kangaroo", "cat", "fox"]


@pytest.mark.parametrize("animal_type", ANIMAL_TYPES)
def test_get_animal_facts(client: httpx.Client, animal_type: str):
    """
    This test will check all of the different animal types for the endpoint
    """
    response = client.get(url=BASE_ENDPOINT, params={QUERY_ANIMAL: animal_type})

    assert response.status_code == 200

    for obj in [Animal(**animal) for animal in response.json()]:
        assert obj.animal == animal_type


@pytest.mark.parametrize("animal_type", ["invalid", "string", "used", "in", "query"])
def test_get_animal_facts_invalid_enum(client: httpx.Client, animal_type: str):
    """
    This test will check all of the different animal types for the endpoint
    """
    response = client.get(url=BASE_ENDPOINT, params={QUERY_ANIMAL: animal_type})

    assert response.status_code == 422


@pytest.mark.parametrize("animal_type", ANIMAL_TYPES)
def test_create_animal(client: httpx.Client, animal_type: str):
    """
    basic test for creating a new fact.
    """

    # CREATE THE RESOURCE
    fact = f"Created fact {uuid4()}"
    payload = {"fact": fact, "animal": animal_type}

    created = client.post(url=BASE_ENDPOINT, json=payload)
    assert created.status_code == 201

    obj = Animal(**created.json())
    assert obj.fact == fact
    assert obj.animal == animal_type


@pytest.mark.parametrize("animal_type", ["invalid", "string", "used", "in", "query"])
def test_create_animal_invalid(client: httpx.Client, animal_type: str):
    """
    basic test for creating a new fact.
    with invalid animal types
    """

    # CREATE THE RESOURCE
    fact = f"Created fact {uuid4()}"
    payload = {"fact": fact, "animal": animal_type}

    response = client.post(url=BASE_ENDPOINT, json=payload)

    assert response.status_code == 422
