class DamageCalculator:
    def __init__(self):
        # Tabela de efetividade de tipos
        self.type_chart = {
            'Fogo': {'Fogo': 0.5, 'Água': 0.5, 'Grama': 2.0},  # Exemplo básico de fraquezas/resistências
            'Água': {'Fogo': 2.0, 'Água': 0.5, 'Grama': 0.5},
            'Grama': {'Fogo': 0.5, 'Água': 2.0, 'Grama': 0.5}
        }

    def calculate_damage(self, attack_type: str, defense_type: str, power: int) -> int:
        """Calcula o dano causado por um ataque levando em consideração os tipos de ataque e defesa."""

        effectiveness = self.type_chart[attack_type][defense_type]
        damage = int(power * effectiveness)
        return damage
