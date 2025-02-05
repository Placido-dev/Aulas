import requests

api_url = 'https://pokeapi.co/api/v2/'

def get_pokemon(name):
    url = f'{api_url}/pokemon/{name}'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print('Falha em obter a', response.status_code)

pokemon_name = 'dragonite'
pokemon_info = get_pokemon(pokemon_name)

if pokemon_info:
    print(f'{pokemon_info["name"]}')
    print(f'{pokemon_info["id"]}')
    print(f'{pokemon_info["location_area_encounters"]}')