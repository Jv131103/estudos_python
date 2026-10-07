def maior_sequencia_positivos(lista):
    maior_sequencia = []
    sequencia_atual = []

    for valor in lista:
        if valor > 0:
            sequencia_atual.append(valor)
        else:
            if len(sequencia_atual) > len(maior_sequencia):
                maior_sequencia = sequencia_atual

            sequencia_atual = []

    if len(sequencia_atual) > len(maior_sequencia):
        maior_sequencia = sequencia_atual

    return maior_sequencia


lista = [3, 5, -2, 4, 7, 8, -1, 10, 12]

resultado = maior_sequencia_positivos(lista)

print(f"Maior sequência: {resultado}")
print(f"Tamanho: {len(resultado)}")
