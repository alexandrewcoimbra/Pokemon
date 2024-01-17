class Attack:
    """Classe para representar um ataque de um Pokémon.

    Attributes:
        id (int): ID do ataque.
        nome_ataque (str): Nome do ataque.
        tipo (str): Tipo do ataque (Fogo, Gelo, etc).
        poder (int): Poder do ataque.
    """
    def __init__(self, nome_ataque: str, tipo: str, poder: int, id: int = None) -> None:
        """Inicializa um ataque.

        Args:
            id (int): ID do ataque.
            nome_ataque (str): Nome do ataque.
            tipo (str): Tipo do ataque (Fogo, Gelo, etc).
            poder (int): Poder do ataque.
        """
        self.id = id
        self.nome_ataque = nome_ataque
        self.tipo = tipo
        self.poder = poder

    def __repr__(self) -> str:
        return f"Attack({self.id}, '{self.nome_ataque}')"
