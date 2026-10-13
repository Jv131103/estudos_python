def trocar_elementos_pares(lista):
    i = 0
    while i + 1 < len(lista):  # Poderia tb: while i < len(lista) - 1:
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
        i += 2

    return lista


print(trocar_elementos_pares([10, 20, 30, 40, 50, 60]))
print(trocar_elementos_pares([1, 2, 3, 4, 5]))
