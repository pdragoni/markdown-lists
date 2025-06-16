import re
from extract_content import extract_pokemon


def write_pokemon(file_path, pokemon_list):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    non_legendary = extract_pokemon(file_path, "Não lendários")
    legendary = extract_pokemon(file_path, "Lendários")
    multi = extract_pokemon(file_path, "Multi")
    file = open(pokemon_list, 'w', encoding='utf-8')
    for pokemon in non_legendary:
        file.write(f'non_legendary: {pokemon};\n')
        # file.write(f'{pokemon};\n')
        
    for pokemon in multi:
        file.write(f'multi: {pokemon};\n')
        # file.write(f'{pokemon};\n')
        
    for pokemon in legendary:
        file.write(f'legendary: {pokemon};\n')  
        # file.write(f'{pokemon};\n')
        
    file.close()
    print('File written successfully')


pokemon_list = 'finalList.txt'
file_path = 'pokelist.md'    
write_pokemon(file_path, pokemon_list)
    