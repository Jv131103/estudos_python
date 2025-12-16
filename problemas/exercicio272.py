def ajustar(lista):
    for i in range(len(lista)):
        if isinstance(lista[i], str):
            lista[i] = lista[i].capitalize()
    return lista


def ajustar1(lista):
    novo = []
    for valor in lista:
        novo.append(valor.capitalize())
    return novo


nomes = ["ana", "João", "MARIA"]
print(ajustar(nomes.copy()))
print(ajustar1(nomes.copy()))
