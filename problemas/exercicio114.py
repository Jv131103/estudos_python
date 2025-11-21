frutas = ['  Banana  ', ' Laranja   ', '  Maçã', ' Melão ']

dicionario = {i + 1: frutas[i].strip() for i in range(len(frutas))}
print(dicionario)

dicionario = {str(i): fruta.strip() for i, fruta in enumerate(frutas, start=1)}
print(dicionario)
