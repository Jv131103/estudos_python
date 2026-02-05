from random import randint


def maior_e_menor(limite):
    maior = 0
    menor = 1000

    for _ in range(limite):
        n = randint(0, 1000)
        print(f"N: {n}")

        if n > maior:
            maior = n

        if n < menor:
            menor = n

    return {"maior": maior, "menor": menor}


def maior_e_menor_iteraveis(limite):
    lista = [randint(0, 1000) for i in range(limite)]

    maior = lista[0]
    menor = lista[0]

    for num in lista:
        print(f"N: {num}")

        if num > maior:
            maior = num

        if num < menor:
            menor = num

    return {"maior": maior, "menor": menor}


print(maior_e_menor(10))
print()
print(maior_e_menor_iteraveis(10))
