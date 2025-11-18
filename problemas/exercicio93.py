tupla1 = ('A', 'B', 'A', 'Z', 'Z', 'X', 'A', 'E', 'K', 'G', 'H')

print(f"Tamanho: {len(tupla1)}")
print(f"Tupla ordenada: {tuple(sorted(tupla1))}")
print(f"Ocorrências de A: {tupla1.count("A")}")
print(f"Ocorrências de B: {tupla1.count("B")}")
print(f"Indice de X: {tupla1.index("X")}")
print(f"último elemento: {tupla1[len(tupla1) - 1]}")
