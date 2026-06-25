def meio(lista):
    return lista[len(lista) // 2]


def meio1(lista):
    slow = 0
    fast = 0

    while fast < len(lista) - 1:
        slow += 1
        fast += 2

    return lista[slow]


print(meio([1, 2, 3, 4, 5]))
print(meio([1, 2, 3, 4]))
print(meio([10, 20, 30, 40, 50, 60, 70]))
print()
print(meio1([1, 2, 3, 4, 5]))
print(meio1([1, 2, 3, 4]))
print(meio1([10, 20, 30, 40, 50, 60, 70]))
