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
            for index, pokemon in enumerate(self.pokemons):
                print(f"\t{index} - {pokemon}")

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha seu Pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f"{pokemon_escolhido} eu escolho você!!!")
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("ERRO: Esse jogador não possui Pokémons.")

    
    def batalhar(self, pessoa):
        print(f"{self} iniciou uma batalha com {pessoa}!")
        pessoa.mostrar_pokemons()
        self.escolher_pokemon()


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


    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
        else:
            print("ERRO: Esta pessoa não possui nenhum pokemon.")
