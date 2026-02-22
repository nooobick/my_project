from contextlib import contextmanager
from typing import Generator

import mysql.connector
from mysql.connector import MySQLConnection

from config.db_config import DB_CONFIG


class DatabaseError(Exception):
    """Ошибки работы с базой данных."""


@contextmanager
def db_cursor(commit: bool = False) -> Generator:
    connection: MySQLConnection | None = None
    cursor = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        yield cursor
        if commit:
            connection.commit()
    except mysql.connector.Error as exc:
        if connection and commit:
            connection.rollback()
        raise DatabaseError(str(exc)) from exc
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
