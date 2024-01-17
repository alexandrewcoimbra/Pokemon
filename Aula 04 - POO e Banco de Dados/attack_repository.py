from typing import Any, List
from attack import Attack
import sqlite3

class AttackRepository:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def execute_query(self, query: str, *params: Any) -> None:
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def inserir_ataque(self, attack: Attack) -> Attack:
        query = "INSERT INTO attacks (nome_ataque, tipo, poder) VALUES (?, ?, ?)"
        self.execute_query(query, attack.nome_ataque, attack.tipo, attack.poder)

        attack_id = self.get_last_inserted_id()
        attack.id = attack_id

        return attack

    def obter_ataques(self) -> List[Attack]:
        query = "SELECT * FROM attacks"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [Attack(row[1], row[2], row[3], row[0]) for row in rows]

    def get_last_inserted_id(self) -> int:
        query = "SELECT last_insert_rowid()"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0] if row else None
