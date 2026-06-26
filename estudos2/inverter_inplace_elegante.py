def inverter_in_place(lista):
    if not isinstance(lista, list):
        raise ValueError("O argumento deve ser uma lista")

    tamanho = len(lista)

    # Vamos apenas até a metade da lista
    for i in range(tamanho // 2):
        # O par simétrico de 'i' no final da lista é 'tamanho - 1 - i'
        j = tamanho - 1 - i

        # Fazemos o swap direto
        lista[i], lista[j] = lista[j], lista[i]

    return lista


print(inverter_in_place([1, 2, 3, 4, 5]))
