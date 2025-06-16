import re

regions_data = {}

def extract_pokemon(file_path):
    global regions_data
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract regions and their Pokémon
    
    regions = re.findall(r'<summary>\s*<strong>(.*?)</strong>', content)

    for region in regions:
        non_legendaries = []
        legendaries = []
        multi = []

        region_pattern = re.compile(
            rf'<summary>\s*<strong>{region}</strong>.*?#### Não lendários:\s*>\s*([\w\s.,&;]+);'
            r'(?:.*?#### Multi:\s*>\s*([\w\s.,&;]+);)?'  # Multi section is optional
            r'(?:.*?#### Lendários:\s*>\s*([\w\s.,&;]+);)?'
            r'.*?</details>',
            re.S
        )
        
        match = region_pattern.search(content)
        
        if match:
            non_legendaries = clean_pokemon_names(match.group(1)) if match.group(1) else []
            multi = clean_pokemon_names(match.group(2)) if match.group(2) else []
            legendaries = clean_pokemon_names(match.group(3)) if match.group(3) else []
            
            regions_data[region] = {
                "non_legendary": non_legendaries,
                "multi": multi,
                "legendary": legendaries
            }
            

    return regions_data

def clean_pokemon_names(names_str):
    if names_str:
        return [name.strip().replace('&female', '(F)').replace('&male', '(M)') for name in names_str.strip().split(',')]
    return []

# def print_pokemon(regions_data):
#     if not regions_data:
#         print("No regions found in the file.")
#         return

#     for region, pokemon in regions_data.items():
#         print(f"Region: {region}")

#         # Print Non-Legendary Pokémon
#         non_legendaries = pokemon["non_legendary"]
#         print("Non-Legendary Pokémon:" if non_legendaries else "Non-Legendary Pokémon: None")
#         if non_legendaries:
#             print(', '.join(non_legendaries))

#         # Print Legendary Pokémon
#         legendaries = pokemon["legendary"]
#         print("Legendary Pokémon:" if legendaries else "Legendary Pokémon: None")
#         if legendaries:
#             print(', '.join(legendaries))

#         print()  # Blank line for readability
        

def write_pokemon(file_path, pokemon_list):
    global regions_data
    regions_data = extract_pokemon(file_path)
    print(regions_data)
    with open(pokemon_list, 'w', encoding='utf-8') as file:
        for region, pokemon in regions_data.items():
            file.write(f"Region: {region}\n")
            
            # Write Non-Legendary Pokémon
            non_legendaries = pokemon["non_legendary"]
            file.write("Non-Legendary Pokémon:" if non_legendaries else "Non-Legendary Pokémon: None")
            if non_legendaries:
                file.write(', '.join(non_legendaries))
            file.write('\n')
            
            #Write Multi-Region Pokémon
            multi = pokemon["multi"]
            file.write("Multi-Region Pokémon:" if multi else "Multi-Region Pokémon: None")
            if multi:
                file.write(', '.join(multi))
            file.write('\n')
            
            # Write Legendary Pokémon
            legendaries = pokemon["legendary"]
            file.write("Legendary Pokémon:" if legendaries else "Legendary Pokémon: None")
            if legendaries:
                file.write(', '.join(legendaries))
            file.write('\n\n')
    print('File written successfully')

file_path = 'pokelist.md'  # Replace with your actual file path
pokemon_list = 'finalList.txt'
regions_data = extract_pokemon(file_path)
# print_pokemon(regions_data)
write_pokemon(file_path, pokemon_list)