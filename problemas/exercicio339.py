def maior_sublista(lista):
    maior = []
    atual = []

    for n in lista:
        if n > 0:
            atual.append(n)
        else:
            atual = []
        if len(atual) > len(maior):
            maior = atual[:]

    return maior


print(maior_sublista([1, 2, -1, 3, 4, 5, -2, 6]))
