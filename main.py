import os
import pickle

from pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player: Player):
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

def continuar():
    input("Enter para continuar...")
    os.system('cls')


def salvar_jogo(player: Player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
    except:
        print("Ocorreu um erro ao salvar.")


def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            return player
    except:
        print("Ocorreu um erro ao carregar o jogo.")


if __name__ == "__main__":
    os.system('cls')
    print("------------------------------------------")
    print("Bem vindo ao game Pokemon RPG de terminal!")
    print("------------------------------------------")

    player = carregar_jogo()

    if not player:
        nome = input("\nInsira o seu nome: ")
        player = Player(nome)
        os.system('cls')
        print(f"Olá, {player}, esse é um mundo habitado por Pokémons. A partir de agora, sua missão é se tornar um mestre dos Pokémons.")
        print("Capture o máximo que conseguir e lute com seus inimigos!")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já vi que você tem alguns Pokémons")
            player.mostrar_pokemons()
        else:
            print("Você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!")
            escolher_pokemon_inicial(player)

        print("Como você já possui Pokémon, enfrentará seu arqui-inimigo, o famigerado Gary!!")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)
        continuar()

    while True:
        print("-----------------------")
        print("O que deseja fazer?")
        print("1 - Explorar o mundo")
        print("2 - Lutar com um inimigo")
        print("3 - Ver Podédex")
        print("0 - Sair do jogo")
        escolha = input("Entre com sua escolha: ")

        if escolha == "0": break

        if escolha == "1":
            player.explorar()
            salvar_jogo(player)
            continuar()

        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
            continuar()
        elif escolha == "3":
            os.system('cls')
            player.mostrar_pokemons()
            continuar()
        else:
            print("Escolha inválida!")
            continuar()