"""
This module is meant to represent the ABC pydantic model for all Animals.
"""

from enum import Enum

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class AnimalEnum(str, Enum):
    """
    ENUM for the possible animals to retrieve a fact about.
    """

    BIRD = "bird"
    CAT = "cat"
    DOG = "dog"
    FOX = "fox"
    KANGAROO = "kangaroo"


class FactModel(BaseModel):  # pylint:disable=too-few-public-methods
    """
    Basemodel for Facts.
    """

    id: int
    fact: str
    animal: AnimalEnum
