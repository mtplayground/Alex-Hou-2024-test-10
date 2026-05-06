import os
from contextlib import contextmanager
from typing import Iterator, TypedDict

import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection as PGConnection


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS messages (
    id serial primary key,
    name text not null,
    text text not null,
    created_at timestamptz default now()
)
"""


class MessageRecord(TypedDict):
    id: int
    name: str
    text: str
    created_at: object


def get_database_url() -> str:
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL environment variable is required")
    return database_url


def get_connection() -> PGConnection:
    return psycopg2.connect(get_database_url())


@contextmanager
def connect() -> Iterator[PGConnection]:
    connection = get_connection()
    try:
        yield connection
    finally:
        connection.close()


def initialize_schema() -> None:
    with connect() as connection:
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(SCHEMA_SQL)


def list_messages() -> list[MessageRecord]:
    with connect() as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                """
                SELECT id, name, text, created_at
                FROM messages
                ORDER BY created_at DESC
                """
            )
            rows = cursor.fetchall()
    return [MessageRecord(**row) for row in rows]
