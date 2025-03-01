import re


def extract_pokemon(file_path, category):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regex to find text between '#### category-of-Pokémon:>' and ';'
    
    # pattern = rf'#### {category}:\s*>\s*([\w\s.,;]+);' 
    # # does not find multi-region pokemon

    pattern = rf'#### {category}:\s*>\s*([\w\s.,&;-]+);' 
    # in JS: new RegExp(`#### ${category}:\\s*>\\s*([\\w\\s.,&;-]+);`)
    matches = re.findall(pattern, content, re.S)

    # Clean up the matches to remove trailing commas or whitespace
    cleaned_matches = [match.strip(', ') for match in matches if match]
    return cleaned_matches


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
file_path = 'pokelist.md'
# file_path = 'shinyList.md'
print_pokemon(file_path)