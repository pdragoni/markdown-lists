import re

def extract_pokemon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract regions and their Pokémon
    regions_data = {}
    regions = re.findall(r'<summary>\s*<strong>(.*?)</strong>', content)

    for region in regions:
        # Use regex to find Pokémon specific to the current region
        region_pattern = re.compile(
            rf'<summary>\s*<strong>{region}</strong>.*?#### Não lendários:\s*>\s*([\w\s.,&;]+);.*?#### Lendários:\s*>\s*([\w\s.,&;]+);',
            re.S
        )
        match = region_pattern.search(content)
        
        if match:
            non_legendaries = clean_pokemon_names(match.group(1))
            legendaries = clean_pokemon_names(match.group(2))
            
            regions_data[region] = {
                "non_legendary": non_legendaries,
                "legendary": legendaries
            }

    return regions_data

def clean_pokemon_names(names_str):
    if names_str:
        return [name.strip().replace('&female', '(F)').replace('&male', '(M)') for name in names_str.strip().split(',')]
    return []

def print_pokemon(regions_data):
    if not regions_data:
        print("No regions found in the file.")
        return

    for region, pokemon in regions_data.items():
        print(f"Region: {region}")

        # Print Non-Legendary Pokémon
        non_legendaries = pokemon["non_legendary"]
        print("Non-Legendary Pokémon:" if non_legendaries else "Non-Legendary Pokémon: None")
        if non_legendaries:
            print(', '.join(non_legendaries))

        # Print Legendary Pokémon
        legendaries = pokemon["legendary"]
        print("Legendary Pokémon:" if legendaries else "Legendary Pokémon: None")
        if legendaries:
            print(', '.join(legendaries))

        print()  # Blank line for readability

# Example usage
file_path = 'pokelist.md'  # Replace with your actual file path
regions_data = extract_pokemon(file_path)
print_pokemon(regions_data)