def fibonacci_search(arr, x):

    n = len(arr)

    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm1 + fibMMm2

    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm1 + fibMMm2

    offset = -1

    while fibM > 1:

        i = min(offset + fibMMm2, n - 1)

        if arr[i] < x:

            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1

            offset = i

        elif arr[i] > x:

            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        else:
            return i

    if fibMMm1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1


lista = [2, 4, 7, 10, 15, 21, 30, 45, 60]

valor = 21

indice = fibonacci_search(lista, valor)

print("indice:", indice)
