def encontrar_faltante(numeros):
    for i in range(len(numeros) - 1):
        if numeros[i + 1] > numeros[i] + 1:
            return numeros[i] + 1

    return None


print(encontrar_faltante([10, 11, 12, 14, 15]))
print(encontrar_faltante([1, 2, 3, 4, 5]))
print(encontrar_faltante([3, 4, 8, 9]))
print(encontrar_faltante([1, 10]))
print(encontrar_faltante([7]))
print(encontrar_faltante([]))
print(encontrar_faltante([-5, -4, -2, -1]))
print(encontrar_faltante([100, 101, 102, 104]))
