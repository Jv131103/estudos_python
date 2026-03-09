def counting_sort_digito(lista, exp):

    n = len(lista)
    resultado = [0] * n
    contagem = [0] * 10

    for numero in lista:
        indice = (numero // exp) % 10
        contagem[indice] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    for i in range(n - 1, -1, -1):
        indice = (lista[i] // exp) % 10
        contagem[indice] -= 1
        resultado[contagem[indice]] = lista[i]

    for i in range(n):
        lista[i] = resultado[i]


def radix_sort(lista):

    maior = max(lista)

    exp = 1

    while maior // exp > 0:
        counting_sort_digito(lista, exp)
        exp *= 10

    return lista


lista = [170, 45, 75, 90, 802, 24, 2, 66]

print(radix_sort(lista))
