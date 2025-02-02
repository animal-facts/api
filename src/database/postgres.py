"""
This module is meant to represent the Database handle to PostgreSQL
"""

import os
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Callable, Iterator, Protocol

import psycopg2
from dotenv import load_dotenv
from psycopg2._psycopg import connection, cursor  # pylint:disable=no-name-in-module

load_dotenv()


class DatabaseConnector(Protocol):
    """Defines an interface for database connections (for mocking in tests)."""

    def connect(self, *args: Any, **kwargs: Any) -> connection:
        ...


@dataclass
class DatabaseHandle:
    """
    This is the Postgres database handle
    Used to connect to the database where all Animal facts are located.
    """

    _VALID_KEYS = {
        HOST_KEY := "POSTGRES_HOST",
        PORT_KEY := "POSTGRES_PORT",
        DATABASE_KEY := "POSTGRES_DATABASE",
        USER_KEY := "POSTGRES_USER",
        PASSWORD_KEY := "POSTGRES_PASSWORD",
    }
    host: str
    database: str
    user: str
    password: str
    connector: Callable[..., connection] = psycopg2.connect

    @classmethod
    def from_collector(
        cls,
    ) -> "DatabaseHandle":
        """
        Converts the database config into a DatabaseHandle and returns the class
        """
        return cls(
            host=os.getenv(cls.HOST_KEY, "postgres"),
            database=os.getenv(cls.DATABASE_KEY, ""),
            user=os.getenv(cls.USER_KEY, ""),
            password=os.getenv(cls.PASSWORD_KEY, ""),
        )

    def connect(self) -> connection:
        """
        Create and return a connection to the database
        """
        return self.connector(
            self.host,
            self.database,
            self.user,
            self.password,
        )


@contextmanager
def temporary_connection(
    database_handle: DatabaseHandle,
) -> Iterator[cursor]:
    """
    Connects to the database.
    Returns a cursor.
    Commits the action (If successful)
    Closes the connection.

    Use this instead of DatabaseHandle.connect()
    """
    conn = database_handle.connect()

    with conn.cursor() as _cursor:
        try:
            yield _cursor
            conn.commit()
        finally:
            _cursor.close()
            conn.close()
