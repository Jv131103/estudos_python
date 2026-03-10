import random
from time import sleep


def jogar():

    vitorias = {
        ("tesoura", "papel"),
        ("pedra", "tesoura"),
        ("papel", "pedra")
    }

    opcoes = ["pedra", "papel", "tesoura"]

    pontos_jogador = 0
    pontos_maquina = 0

    while pontos_jogador < 2 and pontos_maquina < 2:

        maquina = random.choice(opcoes)
        jogador = input("Escolha [pedra, papel, tesoura]: ").lower()

        for char in ["jo", "ken", "pô"]:
            print(char, end=" ")
            sleep(0.5)

        print()

        if (jogador, maquina) in vitorias:
            print("Jogador venceu a rodada")
            pontos_jogador += 1

        elif (maquina, jogador) in vitorias:
            print("Máquina venceu a rodada")
            pontos_maquina += 1

        else:
            print("Empate")

        print(f"Placar → Jogador: {pontos_jogador} | Máquina: {pontos_maquina}\n")

    if pontos_jogador == 2:
        print("🏆 Jogador venceu o melhor de 3!")
    else:
        print("🤖 Máquina venceu o melhor de 3!")


jogar()
