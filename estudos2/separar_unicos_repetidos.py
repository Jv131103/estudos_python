def separar_unicos_repetidos(lista):
    unicos = []
    repetidos = []

    contagem = {}

    for valor in lista:
        contagem[valor] = contagem.get(valor, 0) + 1

    for valor, total in contagem.items():
        if total > 1:
            repetidos.append(valor)
        else:
            unicos.append(valor)

    return unicos, repetidos


unicos, repetidos = separar_unicos_repetidos([10, 20, 10, 30, 20, 40, 50, 40])
print(f"Únicos: {unicos}")
print(f"Repetidos: {repetidos}")
