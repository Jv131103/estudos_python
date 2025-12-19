def normalizar_nomes_inplace(lista):
    for i in range(len(lista)):
        if isinstance(lista[i], str):
            lista[i] = lista[i].title().strip()
        else:
            print("Tipo inválido")
            return

    return lista


def normalizar_nomes_novalista(lista):
    novo = []
    for dado in lista:
        if isinstance(dado, str):
            novo.append(dado.title().strip())
        else:
            print("Tipo inválido")
            return

    return novo


lista = ["  ana  ", "JOÃO", "maRia "]
print(normalizar_nomes_inplace(lista.copy()))
print(normalizar_nomes_novalista(lista))
