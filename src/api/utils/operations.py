"""
Holds basic Animal commands.
"""

import dataclasses
from typing import Any

from psycopg2.errors import UniqueViolation

from src.api.models.http.body import AbstractRequestModel, RequestModel

# from src.config.collector import Collector
from src.database.postgres import DatabaseHandle, temporary_connection


@dataclasses.dataclass(frozen=True)
class Operator:
    """
    Abstract Operator class to perform DB actions.
    Allows the api to make CRUD operations to the postgresDB.
    """

    __AVAILABLE_TABLES = {ANIMAL_TABLE := "animals"}
    __VALID_PROPERTIES = {
        ID := "id",
        FACT := "fact",
        ANIMAL := "animal",
    }

    @classmethod
    def count_for_animal(cls, animal: str) -> int | None:
        """
        Returns the count of a table.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            sql = f"SELECT COUNT(*) FROM {cls.ANIMAL_TABLE} WHERE animal='{animal}'"
            cursor.execute(sql)
            row = cursor.fetchone()
        return row[0]

    @classmethod
    def count_all(cls) -> int | None:
        """
        Returns the count of a table.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            sql = f"SELECT COUNT(*) FROM {cls.ANIMAL_TABLE}"
            cursor.execute(sql)
            row = cursor.fetchone()
        return row[0]

    @classmethod
    def get_all_for_animal(cls, animal: str) -> list[dict[str, Any]]:
        """
        Returns a list of all entries in a specific table.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            sql = (
                f"SELECT id,fact,animal FROM {cls.ANIMAL_TABLE} WHERE animal='{animal}'"
            )
            cursor.execute(sql)
            rows = cursor.fetchall()
        if rows is None:
            return [{"ERROR": "Current query returned an empty row."}]
        return [{cls.ID: row[0], cls.FACT: row[1], cls.ANIMAL: row[2]} for row in rows]

    @classmethod
    def get_all(
        cls,
    ) -> list[dict[str, Any]]:
        """
        Returns a list of all facts.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            sql = f"SELECT id,fact,animal FROM {cls.ANIMAL_TABLE}"
            cursor.execute(sql)
            rows = cursor.fetchall()
        if rows is None:
            return [{"ERROR": "Current query returned an empty row."}]
        return [{cls.ID: row[0], cls.FACT: row[1], cls.ANIMAL: row[2]} for row in rows]

    @classmethod
    def get_one(cls, _id: int) -> dict[str, Any]:
        """
        Return the row that belongs to the correct ID key.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            sql = f"SELECT id,fact,animal FROM {cls.ANIMAL_TABLE} WHERE id={_id};"
            cursor.execute(sql)
            row = cursor.fetchone()
        if row is None:
            return {"ERROR": "Current query returned an empty row."}
        return {cls.ID: row[0], cls.FACT: row[1], cls.ANIMAL: row[2]}

    @classmethod
    def get_random_by_animal(cls, animal: str) -> dict[str, Any]:
        """
        Return the row that belongs to the correct ID key.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            sql = f"SELECT id,fact,animal FROM {cls.ANIMAL_TABLE} WHERE animal='{animal}' ORDER BY random() LIMIT 1;"
            cursor.execute(sql)
            row = cursor.fetchone()
        if row is None:
            return {"ERROR": "Current query returned an empty row."}
        return {cls.ID: row[0], cls.FACT: row[1], cls.ANIMAL: row[2]}

    @classmethod
    def get_random(cls) -> dict[str, Any]:
        """
        Return the row that belongs to the correct ID key.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            sql = f"SELECT id,fact,animal FROM {cls.ANIMAL_TABLE} ORDER BY random() LIMIT 1;"
            cursor.execute(sql)
            row = cursor.fetchone()
        if row is None:
            return {"ERROR": "Current query returned an empty row."}

        return {cls.ID: row[0], cls.FACT: row[1], cls.ANIMAL: row[2]}

    @classmethod
    def create(cls, request_body: RequestModel) -> dict[str, Any]:
        """
        Create a new resource to the database.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            try:
                query = "INSERT INTO {table} (fact, animal) VALUES (%s, %s) RETURNING id, fact, animal;".format_map(
                    {"table": cls.ANIMAL_TABLE}
                )
                cursor.execute(query, (request_body.fact, request_body.animal))
                row = cursor.fetchone()
            except UniqueViolation:
                return {"ERROR": "This fact already exists for this animal!"}

        return {cls.ID: row[0], cls.FACT: row[1], cls.ANIMAL: row[2]}

    @classmethod
    def remove_one(cls, _id: int) -> dict[str, Any]:
        """
        Delete a entry from the database if it is found.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            # Find if it exists
            sql_find = f"SELECT id FROM {cls.ANIMAL_TABLE} WHERE id={_id};"
            cursor.execute(sql_find)
            row = cursor.fetchone()
            if row is None:
                return {"ERROR": "Could not find the id"}

            # Delete it
            sql_delete = f"DELETE FROM {cls.ANIMAL_TABLE} WHERE id={_id};"
            cursor.execute(sql_delete)

        return {"SUCCESS": f"Successfully removed fact number: {_id}"}

    @classmethod
    def update_one(cls, _id: int, request: AbstractRequestModel) -> dict[str, Any]:
        """
        Updates a resource in the database.
        """
        with temporary_connection(
            database_handle=DatabaseHandle.from_collector()
        ) as cursor:
            try:
                query = "UPDATE {table} SET fact=(%s) WHERE id={_id} RETURNING id, fact, animal;".format_map(
                    {"table": cls.ANIMAL_TABLE, "_id": _id}
                )
                cursor.execute(query, (request.fact,))
                row = cursor.fetchone()
            except UniqueViolation:
                return {"ERROR": "This fact already exists for this animal!"}

        if row is None:
            return {"ERROR": "Could not find the id"}
        return {cls.ID: row[0], cls.FACT: row[1], cls.ANIMAL: row[2]}
