from typing import Any, List
from battle import Battle
import sqlite3

class BattleRepository:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def execute_query(self, query: str, *params: Any) -> None:
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()