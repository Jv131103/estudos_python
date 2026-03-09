import math


def jump_search(arr, alvo):

    n = len(arr)
    passo = int(math.sqrt(n))
    prev = 0

    while arr[min(passo, n) - 1] < alvo:
        prev = passo
        passo += int(math.sqrt(n))

        if prev >= n:
            return -1

    for i in range(prev, min(passo, n)):
        if arr[i] == alvo:
            return i

    return -1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(jump_search(lista, 1))
print(jump_search(lista, 3))
print(jump_search(lista, 5))
print(jump_search(lista, 8))
print(jump_search(lista, 10))
