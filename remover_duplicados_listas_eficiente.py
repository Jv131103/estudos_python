def remover1(lista):
    novo = []
    for valor in lista:
        if valor not in novo:
            novo.append(valor)
    return novo


def remover2(lista):
    d = {}
    for valor in lista:
        d[valor] = d.get(valor, 0) + 1

    novo = []
    for valor in d:
        novo.append(valor)

    return novo


def remover3(lista):
    return list(dict.fromkeys(lista))


def remover4(lista):
    visto = set()
    write = 0  # posição onde o próximo valor único deve ser escrito

    for read in range(len(lista)):
        if lista[read] not in visto:
            visto.add(lista[read])
            lista[write] = lista[read]
            write += 1

    # remove o "lixo" sobrando no final da lista
    del lista[write:]
    return lista


print(remover1([1, 2, 2, 3, 1, 4, 3]))
print(remover2([1, 2, 2, 3, 1, 4, 3]))
print(remover3([1, 2, 2, 3, 1, 4, 3]))
print(remover4([1, 2, 2, 3, 1, 4, 3]))
