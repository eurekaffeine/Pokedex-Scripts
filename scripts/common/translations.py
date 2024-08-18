import json
import os

def abilities():
    path = os.path.join(os.path.dirname(__file__), '../../assets/translations/ability-names-translation.json')
    with open(path, 'r') as f:
        return json.load(f)

def pokemons():
    path = os.path.join(os.path.dirname(__file__), '../../assets/translations/pokemon-names-translation.json')
    with open(path, 'r') as f:
        return json.load(f)

def ability(id):
    return abilities().get(str(id), None)

def pokemon(id):
    return pokemons().get(str(id), None)