from random import randint


def simular_dado():
    print("**" * 30)
    print("JOGO DO DADO")
    print("==" * 30)
    print("Digite a opção [1 - 6] para jogar")
    print("Digite 0 para sair da partida")
    print("==" * 30)
    qtd_acertos = 0
    qtd_jogadas = 0
    while True:
        try:
            opcao_jogador = int(input("Digite a opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao_jogador <= 0 or opcao_jogador > 6:
            break

        maquina_simulou = randint(1, 6)
        print(f"A máquina sorteou: {maquina_simulou}")

        if opcao_jogador == maquina_simulou:
            print("Vitória +1 ponto adicionado")
            qtd_acertos += 1
        else:
            print("Que pensa, você não ganhou essa")
        print("--" * 30)

        qtd_jogadas += 1

    print(f"Quantidade de acertos: {qtd_acertos}")
    print(f"Quantidade de partidas: {qtd_jogadas}")


simular_dado()
