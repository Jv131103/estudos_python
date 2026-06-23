def tem_par_com_soma(lista, x):
    i = 0
    j = len(lista) - 1

    while i <= j:
        soma = lista[i] + lista[j]

        if soma == x:
            return True
        elif soma > x:
            j -= 1
        else:
            i += 1

    return False


print(tem_par_com_soma([1, 2, 4, 7, 11, 15], x=15))
