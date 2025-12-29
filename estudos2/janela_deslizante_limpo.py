def maior_soma_janela(lista, k):
    if k <= 0 or k > len(lista):
        return None

    maior = None

    for i in range(len(lista) - k + 1):
        soma = 0
        for j in range(i, i + k):
            soma += lista[j]

        if maior is None or soma > maior:
            maior = soma

    return maior


def maior_soma_janela2(lista, k):
    if k <= 0 or k > len(lista):
        return None

    soma_atual = sum(lista[:k])
    maior = soma_atual

    for i in range(k, len(lista)):
        soma_atual = soma_atual - lista[i - k] + lista[i]
        if soma_atual > maior:
            maior = soma_atual

    return maior


lista = [2, 1, 5, 1, 3, 2]
k = 3
print(maior_soma_janela(lista, k))
print(maior_soma_janela2(lista, k))

lista2 = [2, 1, 5, 1, 3, 2, 10, 12]
k = 3
print(maior_soma_janela(lista2, k))
print(maior_soma_janela2(lista2, k))
