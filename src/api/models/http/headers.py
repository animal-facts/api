"""This module is meant to represent the pydantic base model for the headers of a HEAD request."""

from pydantic import BaseModel, Field  # pylint:disable=no-name-in-module


def kebab_case_generator(string: str) -> str:
    """
    Turn snake_cased python attributes to kebab-cased attributes.
    """
    return string.replace("_", "-")


class HeadRequestHeaders(BaseModel):
    """
    Expected /HEAD request headers.
    """

    content_length: int = Field(
        alias="content-length", alias_generator=kebab_case_generator
    )
    content_type: str = Field(
        alias="content-type", alias_generator=kebab_case_generator
    )
    count: int = Field(alias="count", alias_generator=kebab_case_generator)
    date: str = Field(alias="date", alias_generator=kebab_case_generator)
    server: str = Field(alias="server", alias_generator=kebab_case_generator)
