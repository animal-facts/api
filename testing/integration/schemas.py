"""
Schemas
"""

from enum import Enum
from typing import Any

import httpx
from pydantic import BaseModel  # pylint:disable=no-name-in-module


class AnimalEnum(str, Enum):
    """
    ENUM for the possible animals to retrieve a fact about.
    """

    BIRD = "bird"
    CAT = "cat"
    DOG = "dog"
    FOX = "fox"
    KANGAROO = "kangaroo"


class Animal(BaseModel):
    """
    Animal model for testing
    """

    id: int
    fact: str
    animal: str

    @classmethod
    def create(
        cls,
        endpoint: str,
        payload: dict[str, Any],
    ) -> tuple["Animal", httpx.Response]:
        """
        Creates an animal.
        """
        response = httpx.post(
            url=f"{endpoint}/",
            json=payload,
        )
        the_animal = cls(**response.json())
        return the_animal, response

    @classmethod
    def get_one(
        cls,
        endpoint: str,
        animal_id: int,
    ) -> tuple["Animal", httpx.Response] | httpx.Response:
        """
        Get one animal, given a specific id
        """
        response = httpx.get(url=f"{endpoint}/{animal_id}")
        if response.status_code != 200:
            return response

        the_animal = cls(**response.json())
        return the_animal, response

    @classmethod
    def get_random(
        cls,
        endpoint: str,
    ) -> tuple["Animal", httpx.Response]:
        """
        Get random fact.
        """
        response = httpx.get(url=f"{endpoint}/fact")
        the_animal = cls(**response.json())
        return the_animal, response

    @classmethod
    def update(
        cls,
        endpoint: str,
        animal_id: int,
        payload: dict[str, Any],
    ) -> tuple["Animal", httpx.Response]:
        """
        Update a Animal fact
        """
        response = httpx.patch(url=f"{endpoint}/{animal_id}", json=payload)
        the_animal = cls(**response.json())
        return the_animal, response

    @staticmethod
    def delete(endpoint: str, animal_id: int) -> httpx.Response:
        """
        Returns the response of a DELETE method
        """
        response = httpx.delete(url=f"{endpoint}/{animal_id}")
        return response
