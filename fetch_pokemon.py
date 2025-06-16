import requests
import json

def fetch_released_pokemon():
    url = "https://pogoapi.net/api/v1/released_pokemon.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx and 5xx)
        pokemon_data = response.json()
        print(pokemon_data)

        # new_region = input("Region:")
        # pokemon = input("Pokemon:")

        # for key, value in pokemon_data.items():
        #     if value["pokemon_name"] == pokemon:
        #         print(f'{pokemon} is in the {region} region')
        #         region = value["pokemon_region"]
        #         break


        # Add extra keys to each Pokémon
        for pokemon, value in pokemon_data.items():
            pokemon_id = value["id"]  # Get the Pokémon's National Dex number
            value["region"] = []  # Example additional key

            # Determine the Pokémon's region
            # for region, (start, end) in regions.items():
            #     if start <= pokemon_id <= end:
            #         value["regional_form"] = region
            #         break

        # Save data to a JSON file
        with open("testePokemon.json", "w", encoding="utf-8") as file:
            json.dump(pokemon_data, file, indent=4, ensure_ascii=False)

        print("Data saved to testePokemon.json")
        return pokemon_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    fetch_released_pokemon()
