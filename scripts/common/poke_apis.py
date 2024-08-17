import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def get_ability(id):
    response = requests.get(BASE_URL + f"ability/{id}")
    return response.json()

def get_move(id):
    response = requests.get(BASE_URL + f"move/{id}")
    return response.json()

def get_pokemon(id):
    response = requests.get(BASE_URL + f"pokemon/{id}")
    return response.json()

def get_pokemon_species(id):
    response = requests.get(BASE_URL + f"pokemon-species/{id}")
    return response.json()
