def maior_sequencia_crescente(lista):
    if not lista:
        return [], 0

    maior_sequencia = []
    sequencia_atual = [lista[0]]

    for i in range(1, len(lista)):

        if lista[i] > lista[i - 1]:
            sequencia_atual.append(lista[i])

        else:
            if len(sequencia_atual) > len(maior_sequencia):
                maior_sequencia = sequencia_atual

            sequencia_atual = [lista[i]]

    # Caso a maior sequência termine no final da lista
    if len(sequencia_atual) > len(maior_sequencia):
        maior_sequencia = sequencia_atual

    return maior_sequencia, len(maior_sequencia)


lista = [2, 4, 7, 3, 5, 8, 10, 1, 2]

maior_seq, tamanho = maior_sequencia_crescente(lista)

print(f"Maior sequência crescente: {maior_seq}")
print(f"Tamanho: {tamanho}")
