import random

from pokemon import *


NOMES = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Julia', 'Mariana', 'Rafael', 'Fernanda', 'Gustavo']
POKEMONS = [
    PokemonFogo("Charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle")

]

class Pessoa:
    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if len(self.pokemons) == 0:
            print("Você não possui pokémons!\n")
        else:
            print(f"\nPokémons de {self.nome}:")
            for pokemon in self.pokemons:
                print(f"\t{pokemon}")

    def escolher_pokemon(self):
        self.mostrar_pokemons()
    
    def batalhar(self, pessoa):
        print(f"{self} iniciou uma batalha com {pessoa}!")



class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self} capturou {pokemon}")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome, pokemons)
