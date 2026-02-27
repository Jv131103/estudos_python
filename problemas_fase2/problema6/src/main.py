def remover_duplicatas_inplace(lista):
    i = 0

    while i < len(lista):
        j = i + 1

        while j < len(lista):
            if lista[j] == lista[i]:
                lista.pop(j)  # remove duplicata
            else:
                j += 1

        i += 1

    return lista


def remover_duplicatas_inplace2(lista):
    ja_foi = []
    i = 0
    while i < len(lista):
        if lista[i] not in ja_foi:
            ja_foi.append(lista[i])
            i += 1
        else:
            del lista[i]

    return lista


if __name__ == "__main__":
    entrada = [1, 1, 1, 1, 1, 1, 1]
    print(remover_duplicatas_inplace(entrada.copy()))
    print(remover_duplicatas_inplace2(entrada.copy()))
