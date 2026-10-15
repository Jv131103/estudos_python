def somar_acumulado(lista):
    resultado = [0] * len(lista)

    i = 0

    while i < len(lista):
        j = 0
        while j < i + 1:
            resultado[i] += lista[j]
            j += 1

        i += 1

    return resultado


def somar_acumulado2(lista):
    resultado = [0] * len(lista)

    i = 0
    acumulado = 0

    while i < len(lista):
        acumulado += lista[i]
        resultado[i] = acumulado

        i += 1

    return resultado


lista = [2, 3, 1, 4]

print(somar_acumulado(lista))
print(somar_acumulado2(lista))
