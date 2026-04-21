def binary_search(array):
    i = 0
    j = len(array) - 1

    while i < j:
        meio = (i + j) // 2
        if array[meio] > array[j]:
            i = meio + 1
        else:
            j = meio

    return i


print(binary_search([4, 5, 6, 7, 0, 1, 2]))
