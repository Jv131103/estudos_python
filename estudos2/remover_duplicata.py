def remover_duplicata(lista):
    novo = []

    for valor in lista:
        if valor not in novo:
            novo.append(valor)

    return novo


def remover_duplicata2(lista):
    d = {}

    novo = []

    for valor in lista:
        d[valor] = d.get(valor, 0) + 1

    for valor in d:
        novo.append(valor)

    return novo


def remover_duplicata_pythonica(lista):
    # Cria o dicionário com chaves únicas e converte direto para lista
    return list(dict.fromkeys(lista))


def remover_duplicata_com_set(lista):
    return list(set(lista))


print(remover_duplicata([3, 1, 2, 3, 4, 1, 5]))
print(remover_duplicata2([3, 1, 2, 3, 4, 1, 5]))
print(remover_duplicata_pythonica([3, 1, 2, 3, 4, 1, 5]))
# Não segue a ordem dos itens originais, mas remove duplicadas
# print(remover_duplicata_com_set([3, 1, 2, 3, 4, 1, 5]))
