

pokemons = (
    ("Pikachu", "Elétrico"),
    ("Bulbasaur", "Planta"),
    ("Charmander", "Fogo"),
    ("Squirtle", "Água"),
    ("Gloom", "Planta"),
    ("Geodude", "Elétrico"),
    ("Psyduck", "Água"),
    ("Arcanine", "Fogo"),
    ("Poliwrath", "Água"),
    ("Vulpix", "Fogo")
)

tipo_escolhido = input("Digite um tipo de Pokémon: ").lower()

pokemons_do_tipo = [pokemon[0] for pokemon in pokemons if pokemon[1].lower() == tipo_escolhido]

quantidade = len(pokemons_do_tipo)

if quantidade == 0:
    print(f"Não há pokémons do tipo {tipo_escolhido}.")
else:
    print(f"Quantidade de pokémons do tipo {tipo_escolhido}: {quantidade}")
    print("Pokémons do tipo escolhido:")
    for pokemon in pokemons_do_tipo:
        print(pokemon)