from pokemon import Pokemon
from attack import Attack
from battle import Battle
from damage_calculator import DamageCalculator
from pokemon_repository import PokemonRepository
from attack_repository import AttackRepository
from database_initializer import InicializadorBD

# Inicializando o banco de dados
db_name = 'pokemon_database.db'
InicializadorBD.criar_tabelas(db_name)

# Inicializando os repositórios
pokemon_repo = PokemonRepository(db_name)
attack_repo = AttackRepository(db_name)

# Verificando se há Pokémon no banco de dados
pokemon_list = pokemon_repo.obter_pokemon()
if not pokemon_list:
    # Se não houver Pokémon, cria e insere no banco de dados
    charmander = Pokemon("Charmander", "Fogo", 50)
    squirtle = Pokemon("Squirtle", "Água", 50)
    charmander = pokemon_repo.inserir_pokemon(charmander)
    squirtle = pokemon_repo.inserir_pokemon(squirtle)
else:
    charmander, squirtle = pokemon_list[0], pokemon_list[1]

# Verificando se há ataques no banco de dados
attack_list = attack_repo.obter_ataques()
if not attack_list:
    # Se não houver ataques, cria e insere no banco de dados
    ember = Attack("Ember", "Fogo", 10)
    water_gun = Attack("Water Gun", "Água", 10)
    ember = attack_repo.inserir_ataque(ember)
    water_gun = attack_repo.inserir_ataque(water_gun)
else:
    ember, water_gun = attack_list[0], attack_list[1]

# Obtendo Pokémon e ataques do banco de dados
pokemon_list = pokemon_repo.obter_pokemon()
attack_list = attack_repo.obter_ataques()

# Selecionando os dois primeiros Pokémon e os dois primeiros ataques para a batalha
charmander = pokemon_list[0]
squirtle = pokemon_list[1]
ember = attack_list[0]
water_gun = attack_list[1]

# Adicionando ataques aos Pokémon
charmander.ataques.append(ember)
squirtle.ataques.append(water_gun)

# Inicializando a batalha
battle = Battle(charmander, squirtle)

# Inicializando o DamageCalculator
calculator = DamageCalculator()

# Simulando a batalha por alguns turnos
for i in range(3):
    print(f"Turno {i + 1}:")
    print(battle.start_battle())
    print("")

    # Calculando o dano causado por um ataque
    damage_to_squirtle = calculator.calculate_damage(charmander.ataques[0].tipo, squirtle.tipo, charmander.ataques[0].poder)
    damage_to_charmander = calculator.calculate_damage(squirtle.ataques[0].tipo, charmander.tipo, squirtle.ataques[0].poder)

    # Aplicando o dano aos Pokémon
    squirtle.hp -= damage_to_squirtle
    charmander.hp -= damage_to_charmander

# Verificando o vencedor da batalha...

if charmander.hp <= 0 and squirtle.hp <= 0:
    print("A batalha terminou em empate!")
elif charmander.hp <= 0:
    print(f"{squirtle.nome_pokemon} venceu a batalha!")
elif squirtle.hp <= 0:
    print(f"{charmander.nome_pokemon} venceu a batalha!")
else:
    print("A batalha ainda não terminou!")