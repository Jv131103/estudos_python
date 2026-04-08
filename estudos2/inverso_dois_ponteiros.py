def inverter(lista):
    i = 0
    j = len(lista) - 1

    while i <= j:
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1

    return lista


def inverter2(numero):
    negativo = numero < 0
    numero = abs(numero)
    reverse = 0
    while numero > 0:
        ultimo = numero % 10
        reverse = 10 * reverse + ultimo
        numero //= 10

    return -reverse if negativo else reverse


print(inverter([1, 2, 3, 4, 5]))
print(inverter2(12345))
