import random
from time import sleep


def jogar():
    vitorias = {
        ("tesoura", "papel"),
        ("pedra", "tesoura"),
        ("papel", "pedra")
    }

    emojis = {
        "pedra": "🪨",
        "papel": "📄",
        "tesoura": "✂️"
    }

    escolha = ["pedra", "papel", "tesoura"]

    pontos_jogador = 0
    pontos_maquina = 0
    empates = 0

    print("**" * 20)
    while True:
        maquina = random.choice(escolha)
        jogador = input("Escolha: [pedra, papel, tesoura, sair] ").lower()

        if jogador == "sair":
            print("Fim de jogo!")
            break
        elif jogador not in escolha:
            print("Escolha apenas 'pedra', 'papel' ou 'tesoura'")
            continue

        print()
        for char in ["jô", "key", "pô"]:
            print(char, end=" ")
            sleep(0.5)
        print("\n")

        print("--" * 20)
        print(f"Jogador jogou {emojis[jogador]}  e máquina jogou {emojis[maquina]}")
        print("--" * 20)

        if (jogador, maquina) in vitorias:
            print("Vitória do jogador")
            pontos_jogador += 1
        elif (maquina, jogador) in vitorias:
            print("Vitória da máquina")
            pontos_maquina += 1
        else:
            print("Empate")
            empates += 1
        print("**" * 20)

    print("\n===== PLACAR FINAL =====")
    print(f"Acertos do Jogador: {pontos_jogador}")
    print(f"Acertos da Máquina: {pontos_maquina}")
    print(f"Empates: {empates}")
    print()

    if pontos_jogador > pontos_maquina:
        print("Parabéns, você é o campeão 🏆")
    elif pontos_maquina > pontos_jogador:
        print("Vitória das máquinas! 🤖")
    else:
        print("Nenhum vencedor!")


jogar()
