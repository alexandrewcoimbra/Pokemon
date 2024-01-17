from typing import Any, List
import sqlite3

class DatabaseRepository:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def execute_query(self, query: str, *params: Any) -> None:
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def fetch_all(self, query: str, *params: Any) -> List[Any]:
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        connection.close()
        return rows

    def fetch_one(self, query: str, *params: Any) -> Any:
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        row = cursor.fetchone()
        connection.close()
        return row
