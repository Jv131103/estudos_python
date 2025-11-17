lista = [
    'a', 'a', 'a',
    'b', 'c', 'k',
    'a', 1, 2, 3, 4,
    'j', 'l', 'm',
]

lista2 = lista[::]

# versao 1
novo = []

for valor in lista:
    if valor not in novo:
        novo.append(valor)

print(novo)

print()

# Versão 2
lista = list(set(lista2))
print(lista)
