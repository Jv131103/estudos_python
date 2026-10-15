def produto_exceto_atual(lista):
    i = 0
    j = 0
    resultado = []
    mult = 1
    while i < len(lista):
        if j < len(lista):
            if j != i:
                mult *= lista[j]
            j += 1
        else:
            resultado.append(mult)
            mult = 1
            j = i
            i += 1

    return resultado


lista = [1, 2, 3, 4]
print(produto_exceto_atual(lista))
