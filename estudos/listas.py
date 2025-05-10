# Uma lista é uma coleção mutável e ordenada de elementos.
# Isso quer dizer que:
#  - Podemos acessar os itens por índice.
#  - Podemos modificar, adicionar e remover itens.
#  - Listas são objetos do tipo list.

lista = [1, 2, 3]
print(type(lista))  # <class 'list'>

# Listas podem conter qualquer tipo de dado, inclusive diferentes tipos juntos:
misturada = [1, "texto", True, 3.14, [1, 2]]
print(misturada)

# Índices e Fatiamento
numeros = [10, 20, 30, 40, 50]

print(numeros[0])     # 10
print(numeros[-1])    # 50 (último)

print(numeros[:3])    # [10, 20, 30]
print(numeros[2:])    # [30, 40, 50]
print(numeros[::-1])  # [50, 40, 30, 20, 10]

# Modificando elementos
numeros[1] = 99
print(numeros)  # [10, 99, 30, 40, 50]

# Adicionando elementos
numeros.append(60)     # Adiciona no fim
numeros.insert(0, 5)   # Insere na posição 0
print(numeros)

# Removendo elementos
numeros.remove(99)     # Remove o primeiro 99
ultimo = numeros.pop()  # Remove e retorna o último
print(ultimo)
print(numeros)

# Deletando por índice
del numeros[1]
print(numeros)

# Repetição e concatenação
lista = [1, 2]
print(lista * 3)  # [1, 2, 1, 2, 1, 2]
print(lista + [3, 4])  # [1, 2, 3, 4]

# Verificando valores
print(3 in lista)    # False
print(2 in lista)    # True

# Tamanho
print(len(lista))  # 2

# Iterando com for
for item in ["A", "B", "C"]:
    print(item)

# Iterando com while
i = 0
lista = ['A', 'B', 'C']
while i < len(lista):
    print(lista[i])
    i += 1

# Com enumerate para pegar índice + valor
for i, v in enumerate(["a", "b", "c"]):
    print(f"{i} → {v}")

# Compreensões de Lista (List Comprehensions)
quadrados = [x * x for x in range(5)]
print(quadrados)

pares = [x for x in range(10) if x % 2 == 0]
print(pares)

# Métodos importantes

numeros = [1, 4, 2, 8, 5]
print(min(numeros))       # 1
print(max(numeros))       # 8
print(sum(numeros))       # 20
print(sorted(numeros))    # [1, 2, 4, 5, 8]

numeros.sort()            # Ordena em ordem crescente
print(numeros)

numeros.reverse()         # Inverte a ordem atual
print(numeros)

# count e index
letras = ["a", "b", "a", "c"]
print(letras.count("a"))   # 2
print(letras.index("b"))   # 1

# Copiando listas
lista1 = [1, 2, 3]
lista2 = lista1.copy()     # lista2 é uma cópia, não a mesma referência
lista2.append(4)
print(lista1)  # [1, 2, 3]
print(lista2)  # [1, 2, 3, 4]

# Limpando a lista
lista2.clear()
print(lista2)  # []

# Aninhadas
matriz = [[1, 2], [3, 4]]
print(matriz[0][1])  # 2

# unpacking
dados = [10, 20, 30]
a, b, c = dados
print(a, b, c)

# unpacking com *
a, *resto = [1, 2, 3, 4]
print(a)       # 1
print(resto)   # [2, 3, 4]

# Convertendo string para lista
texto = "Python"
lista = list(texto)
print(lista)  # ['P', 'y', 't', 'h', 'o', 'n']

# Split → Quebra string em lista
nomes = "Ana,Bia,Carlos".split(",")
print(nomes)

# Join → Junta lista em string
texto = ", ".join(["maçã", "banana", "uva"])
print(texto)

# Exercício prático simples:
# Somando elementos de uma lista
numeros = [1, 2, 3, 4, 5]
soma = 0
for n in numeros:
    soma += n
print("Soma:", soma)

# Transformando valores em outra lista
dobros = []
for n in numeros:
    dobros.append(n * 2)
print(dobros)

# Equivalente com list comprehension:
dobros = [n * 2 for n in numeros]
print(dobros)

# Criando uma matriz 4 x 3
matriz = []
for i in range(4):  # 4 linhas
    linha = []
    for j in range(3):  # 3 colunas
        valor = float(input(f"Digite o valor para posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"Linha [{i}] coluna [{j}] = {matriz[i][j]}")

# Dicas finais:
# - Use o copy() para cópia independente.
# - Use o in para ver se o valor está na lista.
# - Evite remover elementos de uma lista enquanto itera sobre ela.
