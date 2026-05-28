import random
import time


def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def selection_sort(lista):
    n = len(lista)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and chave < lista[j]:

            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista


def comparar(tamanho=1000):
    # Gera a mesma lista para os três
    original = [random.randint(0, 10000) for _ in range(tamanho)]

    for nome, funcao in [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
    ]:
        lista = original.copy()
        inicio = time.time()
        resultado = funcao(lista)
        fim = time.time()
        print(f"{nome}: {fim - inicio:.4f}s | Primeiro: {resultado[0]} | Último: {resultado[-1]}")


comparar()
