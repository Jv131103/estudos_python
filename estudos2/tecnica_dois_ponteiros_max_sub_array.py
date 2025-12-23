def max_soma(lista, k):
    atual = sum(lista[:k])
    max_soma = atual

    for i in range(k, len(lista)):
        atual += lista[i] - lista[i - k]
        max_soma = max(max_soma, atual)

    return max_soma


lista = list(range(10))
print(max_soma(lista, 2))
