import requests
import json
pokemon = requests.get('http://pokeapi.co/api/v2/pokemon/1/')
ability = requests.get('http://pokeapi.co/api/v2/ability/1/')
json_1 = json.loads(pokemon.content)
json_2 = json.loads(ability.content)
print("Pokemon Name: " + json_1['name'])
print("Pokemon Ability: " + json_2['name'])