import random


def mega_sena():
    numeros = []

    while len(numeros) < 6:
        sorteio = random.randint(1, 60)
        if sorteio not in numeros:
            numeros.append(sorteio)

    numeros.sort()

    # apenas para exibir bonito
    saida = " ".join(map(str, numeros))

    print("Os números sorteados foram:")
    print("\t", saida)

    return numeros


mega_sena()
