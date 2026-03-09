def heapify(lista, n, i):

    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]:
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]:
        maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)


def heap_sort(lista):

    n = len(lista)

    # construir heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # extrair elementos
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)

    return lista


lista = [4, 10, 3, 5, 1]

print(heap_sort(lista))
