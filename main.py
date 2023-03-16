from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player: Player):
    print(f"Olá {player}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!")

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Entre com a opção desejada: ")
    print("1 - ", pikachu)
    print("2 - ", charmander)
    print("3 - ", squirtle)

    while True:
        escolha = input("")

        match escolha:
            case "1": player.capturar(pikachu); break
            case "2": player.capturar(charmander); break
            case "3": player.capturar(squirtle); break
    
    player.mostrar_pokemons()
            


player = Player("Thiago")
player.capturar(PokemonFogo("Charmander",level=1))

inimigo1 = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])

player.batalhar(inimigo1)