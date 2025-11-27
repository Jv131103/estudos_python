import random


def jogo_advinhacao():
    cont = 1
    acertos = 0
    print("**" * 30)
    print("JOGO DE ADVINHAÇÃO")
    print("==" * 30)
    print("Digite a opção [1 - 50] para jogar")
    print("Digite 0 para sair da partida")
    print("==" * 30)
    while cont <= 15:
        try:
            opcao_jogador = int(input(f"Digite a opção {cont}: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao_jogador <= 0 or opcao_jogador > 50:
            print("Erro por opcao inválida, encerrando o jogo!")
            break

        maquina_simulou = random.randint(1, 50)

        if opcao_jogador == maquina_simulou:
            print("Parabéns você acertou! +1 ponto")
            acertos += 1
        elif opcao_jogador > maquina_simulou:
            diferenca = opcao_jogador - maquina_simulou
            print(f"Errou por {diferenca}. Você digitou MAIOR.")
        else:
            diferenca = maquina_simulou - opcao_jogador
            print(f"Errou por {diferenca}. Você digitou MENOR.")

        print(f"A máquina sorteou: {maquina_simulou}")
        print("--" * 30)
        cont += 1

    print(f"Quantidade de acertos: {acertos}")


jogo_advinhacao()
