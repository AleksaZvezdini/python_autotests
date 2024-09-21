import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '865b98a7d3d022956418de002707a113'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4932'

### ЗАДАНИЕ №2 ###

#GET /trainers status 200
def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

#GET /trainers response contains a lot of parameters, include trainer_name
@pytest.mark.parametrize('key, value', [
    ('trainer_name','BugFinder'), 
    ('level', '5'), 
    ('id', '4932'), 
    ('is_premium', True), 
    ('city', 'Velsk')])
def test_all_parametrs(key, value): 
    response_my_trainer_name = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_my_trainer_name.json()['data'][0][key] == value

#My pokemon array contains Autocreate's name
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    trainers_names = [n['name'] for n in response_get.json()['data']]
    assert any(t == 'Autocreate' for t in trainers_names)

