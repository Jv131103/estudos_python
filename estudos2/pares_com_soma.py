def pares_com_soma(lista, alvo):
    pares_distintos = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):

            if lista[i] + lista[j] == alvo:
                par = [lista[i], lista[j]]

                inverso = [lista[j], lista[i]]

                if par not in pares_distintos and inverso not in pares_distintos:
                    pares_distintos.append(par)

    return pares_distintos


lista = [2, 7, 11, 15, 3, 6, 4]
alvo = 9

for distintos in pares_com_soma(lista, alvo):
    print(distintos)
