def mover_zeros(lista):
    slow = 0

    for fast in range(len(lista)):
        if lista[fast] != 0:
            lista[slow], lista[fast] = lista[fast], lista[slow]
            slow += 1

    return lista


print(mover_zeros([1, 3, 12, 0, 0]))
print(mover_zeros([0, 1, 0, 3, 12]))
