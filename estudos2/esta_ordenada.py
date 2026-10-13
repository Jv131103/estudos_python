def esta_ordenada(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            return False

        i += 1

    return True


print(esta_ordenada([1, 2, 3, 4, 5]))
print(esta_ordenada([5, 4, 3, 2, 1]))
print(esta_ordenada([1, 2, 2, 3, 5]))
print(esta_ordenada([1, 4, 3, 5]))
print(esta_ordenada([10]))
print(esta_ordenada([]))
