from pokemon import Pokemon

class Battle:
    def __init__(self, player1: Pokemon, player2: Pokemon) -> None:
        self.player1 = player1
        self.player2 = player2

    def calcular_dano(self, atacante: Pokemon, defensor: Pokemon) -> int:
        # Definir a eficácia dos tipos dos ataques
        eficacia = {
            'Fogo': {'Água': 2, 'Planta': 0.5},  # Exemplo: Fogo é fraco contra Água e resistente contra Planta
            'Água': {'Fogo': 2, 'Planta': 0.5},  # Exemplo: Água é fraca contra Fogo e resistente contra Planta
            'Planta': {'Fogo': 2, 'Água': 0.5}  # Exemplo: Planta é fraca contra Fogo e resistente contra Água
        }

        # Verificar a eficácia do ataque do atacante contra o tipo do defensor
        eficacia_ataque = eficacia.get(atacante.tipo, {}).get(defensor.tipo, 1)

        # Calcular o dano base (apenas um exemplo, pode ser mais complexo na realidade)
        dano_base = 10  # Valor base de dano

        # Calcular o dano considerando a eficácia do ataque
        dano = int(dano_base * eficacia_ataque)

        return dano

    def start_battle(self) -> str:
        # Calcular o dano causado pelo player1 ao player2
        dano_do_player1 = self.calcular_dano(self.player1, self.player2)

        # Calcular o dano causado pelo player2 ao player1 (vamos supor que seja o mesmo)
        dano_do_player2 = self.calcular_dano(self.player2, self.player1)

        # Realizar a batalha
        if dano_do_player1 > dano_do_player2:
            return f"{self.player1.nome_pokemon} venceu a batalha!"
        elif dano_do_player2 > dano_do_player1:
            return f"{self.player2.nome_pokemon} venceu a batalha!"
        else:
            return "A batalha terminou em empate!"
