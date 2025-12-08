def contar_listas(lista):
    total = 0
    for item in lista:
        if isinstance(item, list):
            total += 1
            total += contar_listas(item)
    return total


lista = [1, [2, 3], 4, [5, [6, 7]]]
print(contar_listas(lista))  # 3
