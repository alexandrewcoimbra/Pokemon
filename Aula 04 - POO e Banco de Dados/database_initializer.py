"""
Classe responsável por criar o banco de dados e as tabelas necessárias para armazenar 
os dados. É uma classe que segue o princípio de responsabilidade única ao encapsular
a lógica de inicialização do banco de dados.
"""

import sqlite3

class InicializadorBD:
    @staticmethod
    def criar_tabelas(db_name: str):
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_pokemon TEXT NOT NULL,
                tipo TEXT NOT NULL,
                hp INTEGER NOT NULL 
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_ataque TEXT NOT NULL,
                tipo TEXT NOT NULL,
                poder INTEGER NOT NULL 
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemon_ataques (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pokemon_id INTEGER NOT NULL,
                ataque_id INTEGER NOT NULL,
                FOREIGN KEY (pokemon_id) REFERENCES pokemons(id),
                FOREIGN KEY (ataque_id) REFERENCES ataques(id)
            );
        """)
        connection.commit()
        connection.close()