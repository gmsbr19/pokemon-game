import sys
import random
sys.stdout.reconfigure(encoding='utf-8')

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie
        
    def __str__(self):
        return f"{self.nome}[{self.level}]"

    def atacar(self, pokemon):
        print(f"{self} atacou {pokemon}!")

class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print(f"{self} deu um choque em {pokemon}")

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print(f"{self} lançou uma bola de fogo na cabeça de {pokemon}")

class PokemonAgua(Pokemon):
    tipo = "agua"

    def atacar(self, pokemon):
        print(f"{self} lançou um jato d'água em {pokemon}")


charmander = PokemonFogo("charmander")
squirtle = PokemonAgua("Squirtle")
pikachu = PokemonEletrico("Pikachu")