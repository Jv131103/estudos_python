matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lista = [matriz[i][j] for i in range(len(matriz)) for j in range(len(matriz))]
print(lista)
print(sum(lista))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista = [numero for linha in matrix for numero in linha]
soma = sum(lista)
print(lista)
print(soma)
