
def diferencas_consecutivas(lista):
    resultado = [0] * len(lista)

    for i in range(1, len(lista)):
        resultado[i] = lista[i] - lista[i - 1]

    return resultado


print(diferencas_consecutivas([10, 15, 12, 20, 18]))
print(diferencas_consecutivas([5, 5, 5]))
print(diferencas_consecutivas([7]))
print(diferencas_consecutivas([]))
