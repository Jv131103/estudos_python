def maior_menor_manual(lista):
    """
    Tempo: O(n) (1 passagem)

    Espaço extra: O(1)
    """
    maior = lista[0]
    menor = lista[0]

    for indice in range(1, len(lista)):
        if lista[indice] > maior:
            maior = lista[indice]

        if lista[indice] < menor:
            menor = lista[indice]

    return menor, maior


def maior_menor_recursivo(lista, i=0, maior=0, menor=0):
    """
    Tempo: O(n) (1 chamada por elemento)

    Espaço extra: O(n) (pilha de recursão)
    """
    if i == 0:
        maior = menor = lista[i]

    if i == len(lista):
        return menor, maior

    if lista[i] > maior:
        maior = lista[i]

    if lista[i] < menor:
        menor = lista[i]

    return maior_menor_recursivo(lista, i=i + 1, maior=maior, menor=menor)


def maior_menor_ordenado_inplace(lista):
    """
    Tempo: O(n log n) (sort do Python — Timsort)

    Espaço extra: O(1) extra na lista (mas o sort pode usar memória auxiliar
    interna; em Big-O, costuma-se citar O(n) no pior caso para auxiliares do
    algoritmo, dependendo da implementação)
    """
    lista.sort()
    return lista[0], lista[-1]


def maior_menor_ordenado_nao_inplace(lista):
    """
    Tempo: O(n log n) (sorted)

    Espaço extra: O(n) (cria nova lista ordenada)
    """
    lista = sorted(lista)
    return lista[0], lista[-1]


def maior_menor_ordenado_pythonico(lista):
    """
    Tempo: O(n log n) duas vezes (porque ordena duas vezes) → continua
    O(n log n), mas com constante bem pior

    Espaço extra: O(n) duas vezes (duas listas temporárias; pico ainda O(n))
    """
    return min(sorted(lista)), max(sorted(lista))


def maior_menor_pythonico(lista):
    """
    Tempo: O(n) + O(n) = O(n) (duas passagens)

    Espaço extra: O(1)
    """
    return min(lista), max(lista)


if __name__ == "__main__":
    lista = [9, 2, 1, 0, 5, 6, 10, 11, 12]
    print(maior_menor_manual(lista))
    print(maior_menor_recursivo(lista))
    print(maior_menor_ordenado_nao_inplace(lista))
    print(maior_menor_pythonico(lista))
    print(maior_menor_ordenado_inplace(lista))
