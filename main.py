import requests
from random import randint as r

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '865b98a7d3d022956418de002707a113'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4932'

#GET /pokemons
res_get_pokemons = requests.get(url = f'{URL}/pokemons', headers=HEADER, params={'trainer_id':TRAINER_ID})
first_pokemon_id = res_get_pokemons.json()['data'][0]['id']


### ЗАДАНИЕ №1 ###

#POST /pokemons
body_create_pokemon = {
    "name": "PythonPokemon",
    "photo_id": r(1,1000)
}
response = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create_pokemon)
print(f'Создание покемона: {response.json()}')

#PUT /pokemons
body_change_pokemon = {
  "pokemon_id": first_pokemon_id,
  "name": "PythonPokemon",
  "photo_id": r(1,1000),
}
response = requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_change_pokemon)
print(f'Смена имени покемона: {response.json()}')

#POST /trainers/add_pokeball
body_add_pokeball = {
  "pokemon_id": first_pokemon_id
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(f'Поймать покемона в покебол: {response.json()}')
