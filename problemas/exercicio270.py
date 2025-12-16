def existe(lista, valor):
    for x in lista:
        if x == valor:
            return True
    return False


valores = [chr(num) for num in range(97, 122)]
print(existe(valores, 's'))
print(existe(valores, 'S'))
