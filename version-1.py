import re
from extract_content import extract_pokemon


def print_pokemon(file_path):
    non_legendary = extract_pokemon(file_path, "Não lendários")
    legendary = extract_pokemon(file_path, "Lendários")
    multi = extract_pokemon(file_path, "Multi")

    print("Non-Legendary Pokémon:\n")
    for pokemon in non_legendary:
        print(pokemon)
        
    print("\nMulti-region Pokémon:\n")
    for pokemon in multi:
        print(pokemon)

    print("\nLegendary Pokémon:")
    for pokemon in legendary:
        print(pokemon)


# file_path and print_pokemon()
pokemon_list = 'finalList.txt'
file_path = 'pokelist.md'
# file_path = 'shinyList.md'
print_pokemon(file_path)
