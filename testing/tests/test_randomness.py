"""
Testing module for Birds.
"""

import httpx
import pytest

from testing.schemas import Animal

BASE_ENDPOINT = "/facts/"
QUERY_ANIMAL = "animal"
ANIMAL_TYPES = ["bird", "dog", "kangaroo", "cat", "fox"]


def test_random_facts(client: httpx.Client):
    """
    Tests the /facts/random endpoint
    """

    set_of_randomness = set()
    number_of_runs = 50
    for _ in range(number_of_runs):
        response = client.get(url=f"{BASE_ENDPOINT}random")

        obj = Animal(**response.json())
        set_of_randomness.add(obj.animal)
    assert len(set_of_randomness) > 1


@pytest.mark.parametrize("animal_type", ANIMAL_TYPES)
def test_random_facts_specific_animal(client: httpx.Client, animal_type: str):
    """
    Tests the /facts/random endpoint,
    But will only check specific animal type
    """

    set_of_randomness_type = set()
    set_of_randomness_fact = set()
    number_of_runs = 50
    for _ in range(number_of_runs):
        response = client.get(
            url=f"{BASE_ENDPOINT}random", params={QUERY_ANIMAL: animal_type}
        )

        obj = Animal(**response.json())
        assert obj.animal == animal_type
        set_of_randomness_type.add(obj.animal)
        set_of_randomness_fact.add(obj.fact)
    assert len(set_of_randomness_type) == 1
    assert len(set_of_randomness_fact) > 1
