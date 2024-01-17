from typing import Any, List
import sqlite3
from pokemon import Pokemon
from attack import Attack

class PokemonRepository:
    """Repositório de usuários."""
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def executar_query(self, query: str, *params: Any) -> None:
        """Executa uma query no banco de dados.
        
        Args:
            query (str): Query que será executada.
            params (Any): Parâmetros da query.
        """
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def inserir_pokemon(self, pokemon: Pokemon) -> Pokemon:
        """Insere um pokemon no banco de dados. O objeto pokemon é atualizado com o ID do banco.
        
        Args:
            pokemon (Pokemon): Pokemon que será inserido no banco de dados.
        """
        query = "INSERT INTO pokemons (nome_pokemon, tipo, hp) VALUES (?, ?, ?)"
        self.executar_query(query, pokemon.nome_pokemon, pokemon.tipo, pokemon.hp)

        pokemon_id = self.get_ultimo_id_inserido()
        pokemon.id = pokemon_id

        return pokemon

    def atualizar_pokemon(self, pokemon: Pokemon) -> None:
        """Atualiza os dados de um pokemon no banco de dados."""
        query = "UPDATE pokemons SET nome_pokemon = ?, tipo = ?, hp = ? WHERE id = ?"
        self.executar_query(query, pokemon.nome_pokemon, pokemon.tipo, pokemon.hp, pokemon.id)

    def remover_pokemon(self, pokemon: Pokemon) -> None:
        """Remove um pokemon do banco de dados."""
        query = "DELETE FROM pokemons WHERE id = ?"
        self.executar_query(query, pokemon.id)

    def obter_pokemon(self) -> List[Pokemon]:
        """Obtém todos os pokemons cadastrados no banco de dados."""
        query = "SELECT * FROM pokemons"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        return [Pokemon(row[1], row[2], row[3], row[0]) for row in rows]
    
    def adicionar_ataque_ao_pokemon(self, pokemon_id: int, ataque_id: int) -> None:
        """Associa um ataque a um Pokémon no banco de dados."""
        query = "INSERT INTO pokemon_ataques (pokemon_id, ataque_id) VALUES (?, ?)"
        self.executar_query(query, pokemon_id, ataque_id)

    def obter_ataques_do_pokemon(self, pokemon_id: int) -> List[Attack]:
        """Obtém todos os ataques associados a um Pokémon."""
        query = "SELECT ataques.* FROM ataques INNER JOIN pokemon_ataques ON ataques.id = pokemon_ataques.ataque_id WHERE pokemon_ataques.pokemon_id = ?"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, (pokemon_id,))
        rows = cursor.fetchall()
        connection.close()
        return [Attack(row[1], row[2], row[3], row[0]) for row in rows]
    
    def get_ultimo_id_inserido(self) -> int:
        """Retorna o ID do último registro inserido no banco de dados."""
        query = "SELECT id FROM pokemons ORDER BY 1 DESC LIMIT 1;"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0]