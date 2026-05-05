import random


def gerar_numero():
    # Retorna uma lista com 4 dígitos únicos aleatórios
    cont = 0

    lista = []
    while cont < 4:
        num = random.randint(0, 9)
        if num in lista:
            continue
        if len(lista) == 0 and num == 0:
            continue
        lista.append(num)
        cont += 1

    return lista


def calcular_resultado(secreto, chute):
    # Retorna (bulls, cows)
    lista = [int(i) for i in str(chute)]
    bulls = 0
    cows = 0
    for x, y in zip(secreto, lista):
        if x == y:
            print(f"bull: {y}")
            bulls += 1
        elif x != y and y in secreto:
            print(f"cow: {y}")
            cows += 1
        else:
            print(f"{y} não encontrado")

    print(f"Você conseguiu {bulls} bulls e {cows} cows")

    return bulls == 4


def tratar_numero(msg):
    while True:
        try:
            dado = int(input("Digite um número de 4 dígitos: [Para sair, digite 0] "))
            if dado != 0 and not (1000 <= dado <= 9999):
                print("Digite numeros entre 1000 e 9999")
                continue
            return dado
        except ValueError:
            print("Digite apenas números!")
            continue


def jogar():
    # Loop principal do jogo
    print("++" * 30)
    print("\tCOWS 🐄 AND BULLS 🐂")
    print("++" * 30)
    secreto = gerar_numero()
    tentativas = 0
    while True:
        num = tratar_numero("Digite numeros de 4 dígitos: [Para sair digite 0]: ")
        if num == 0:
            print("Fim do jogo!")
            break
        tentativas += 1
        resposta = calcular_resultado(secreto, num)
        if resposta:
            print(f"🎉 Parabéns! Você venceu em {tentativas} tentativa(s)!")
            break
        print("Tente novamente")


if __name__ == '__main__':
    jogar()
