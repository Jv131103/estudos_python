def counting_sort(lista):

    if not lista:
        return lista

    maior = max(lista)

    contagem = [0] * (maior + 1)

    for valor in lista:
        contagem[valor] += 1

    resultado = []

    for numero, qtd in enumerate(contagem):
        for _ in range(qtd):
            resultado.append(numero)

    return resultado


lista = [4, 2, 2, 8, 3, 3, 1]

print(counting_sort(lista))
