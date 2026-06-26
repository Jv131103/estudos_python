def meio(lista):
    slow = 0
    fast = 0
    while fast < len(lista):
        slow += 1
        fast += 2
    if len(lista) % 2 == 0:
        return lista[slow]      # primeiro da 2ª metade
    else:
        return lista[slow - 1]  # elemento central


print(meio([1, 2, 3, 4, 5, 6]))
print(meio([1, 2, 3, 4, 5]))
