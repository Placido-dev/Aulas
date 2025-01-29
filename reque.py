import requests

api_url = 'https://pokeapi.co/api/v2/'

def get_pokemon(name):
    url = f'{api_url}/pokemon/{name}'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_name = response.json()
        return pokemon_name
    else:
        print('Falha em obter a', response.status_code)

pokemon_name = 'Dragonite'
pokemon_info = get_pokemon(pokemon_name)
print(pokemon_info)