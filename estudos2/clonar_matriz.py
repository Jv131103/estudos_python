def clonar_matriz_2d(matriz_original):
    copia = []
    for linha in matriz_original:
        nova_linha = []
        for elemento in linha:
            nova_linha.append(elemento)
        copia.append(nova_linha)
    return copia


original = [
    [1, 2, 3],
    [4, 5, 6]
]

clone = clonar_matriz_2d(original)

# Modificando o clone para testar a independência
clone[0][0] = 99

print("Original:", original)  # Mantém [[1, 2, 3], [4, 5, 6]]
print("Clone:", clone)        # Exibe [[99, 2, 3], [4, 5, 6]]
