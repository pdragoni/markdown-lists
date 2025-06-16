import json

def process_pokemon_list(username, list_type):
    # Definição dos arquivos conforme o username
    if username == "1":
        input_file = "released_dragoni.json"
        output_file = "finalListDragoni.txt"
    elif username == "2":
        input_file = "released_marx.json"
        output_file = "finalListMarx.txt"
    else:
        print("Username inválido.")
        return
    
    # Leitura do arquivo JSON
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            pokemon_data = json.load(file)
    except FileNotFoundError:
        print(f"Arquivo {input_file} não encontrado.")
        return
    
    # Definição do formato de escrita conforme a lista desejada
    if list_type == "excluir":
        format_str = "!{id}&"
    elif list_type == "trocar":
        format_str = "{id},"
    else:
        print("Tipo de lista inválido. Use 'excluir' ou 'trocar'.")
        return
    
    # Escrita no arquivo
    with open(output_file, "w", encoding="utf-8") as file:
        for value in pokemon_data.values():
            file.write(format_str.format(id=value["id"]))
    
    print(f"Dados salvos em {output_file}")

# Entrada do usuário
username = input("Digite o número do username (1- dragoni / 2- marx4ever): ")
list_type = input("Digite o tipo de lista ('trocar' ou 'excluir'): ")

process_pokemon_list(username, list_type)
