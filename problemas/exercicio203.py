def filtrar(lista):
    nums = {
        "positivos": [],
        "negativos": [],
        "zeros": []
    }

    for valor in lista:
        if valor == 0:
            nums['zeros'].append(valor)
        elif valor > 0:
            nums["positivos"].append(valor)
        else:
            nums['negativos'].append(valor)

    return nums


lista = [3, -1, 0, 12, -5, 8, 0, 7]
print(filtrar(lista))
