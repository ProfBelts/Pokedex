import requests 
import sys
# import pandas as pd

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    # response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
    # print(response.json())
    pokemon = response.json()

    pokemonName = pokemon["name"]
    pokemonID = pokemon["id"]
    pokemonBaseExp = pokemon["base_experience"]
    firstLetter = pokemonName[0].upper()
    remainingLetter = pokemonName[1:]


    print(f"Name: {firstLetter}{remainingLetter}")
    print(f"ID: {pokemonID}")
    print(f"Base EXP: {pokemonBaseExp}")
if __name__ == "__main__":
    search_pokemon(sys.argv[1])