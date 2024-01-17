"""Modelo de usuário"""

class Pokemon:
    """Classe para representar um usuário.

    Attributes:
        id (int): ID do usuário.
        nome_pokemon (str): Nome do pokemon.
        tipo (str): Tipo do Pokemon (Fogo, Gelo etc).
        hp(int): Quantidade de vida do pokemon.
    """
    def __init__(self, nome_pokemon: str, tipo: str, hp: int, id: int = None) -> None:
        self.id = id
        self.nome_pokemon = nome_pokemon
        self.tipo = tipo
        self.hp = hp
        self.ataques = []  # Adicionando o atributo 'ataques'

    def __repr__(self) -> str:
        return f"Pokemon({self.id}, '{self.nome_pokemon}')"
