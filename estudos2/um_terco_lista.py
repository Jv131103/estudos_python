def um_terco(lista):
    slow = 0
    fast = 0

    while fast < len(lista):
        slow += 1
        fast += 3

    return lista[slow - 1]


print(um_terco([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(um_terco([10, 20, 30, 40, 50, 60]))
