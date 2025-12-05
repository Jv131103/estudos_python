def achatar(lista):
    resultado = []

    for item in lista:
        if isinstance(item, list):
            resultado.extend(achatar(item))  # chama recursivo
        else:
            resultado.append(item)

    return resultado


print(achatar([1, 2, [3, 4], 5]))
# [1, 2, 3, 4, 5]

print(achatar([1, [2, [3, [4, 5]]]]))
# [1, 2, 3, 4, 5]

print(achatar([[1, 2], [], [3, [4, [5]]]]))
# [1, 2, 3, 4, 5]
