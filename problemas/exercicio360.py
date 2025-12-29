def maior_soma_janela(lista, k):
    if not (k > 0) or not (k <= len(lista)):
        return None

    maior = 0
    for i in range(len(lista) - k + 1):
        cont = 0
        soma = 0
        for j in range(i, len(lista)):
            if cont == k:
                break
            soma += lista[j]
            cont += 1

        if soma > maior:
            maior = soma

    return maior


lista = [2, 1, 5, 1, 3, 2]
k = 3
print(maior_soma_janela(lista, k))

lista2 = [2, 1, 5, 1, 3, 2, 10, 12]
k = 3
print(maior_soma_janela(lista2, k))
