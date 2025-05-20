# CONJUNTOS EM PYTHON (set)
# -------------------------

# Conjuntos (sets) são coleções **não ordenadas**, **imutáveis no conteúdo individual**, 
# e **sem elementos duplicados**.
# São muito úteis para:
# - Remover duplicatas
# - Fazer operações matemáticas de conjuntos (união, interseção, diferença etc)
# - Verificar se algo pertence a um grupo (membership test) rapidamente

# É uma estrutura inspirada nos conjuntos da matemática.

# Criando conjuntos:
conjunto1 = {1, 2, 3}
print(conjunto1)  # {1, 2, 3}

# Elementos duplicados são automaticamente ignorados
conjunto2 = {1, 2, 2, 3, 3, 3}
print(conjunto2)  # {1, 2, 3}

# Criando conjunto a partir de uma lista
lista = [1, 2, 2, 3]
conjunto3 = set(lista)
print(conjunto3)  # {1, 2, 3}

# Conjunto vazio:
conjunto_vazio = set()  # NÃO use {} → isso cria um dicionário
print(type(conjunto_vazio))  # <class 'set'>

# Adicionando elementos:
conjunto = {1, 2}
conjunto.add(3)
print(conjunto)  # {1, 2, 3}

# Tentando adicionar um elemento já existente (não acontece nada)
conjunto.add(2)
print(conjunto)  # {1, 2, 3}

# Removendo elementos:
conjunto.remove(2)  # Remove o elemento 2
print(conjunto)  # {1, 3}

# .discard() também remove, mas **não dá erro** se o elemento não existir
conjunto.discard(100)  # Não lança erro

# .pop() remove e retorna um elemento **aleatório** (porque não há ordem)
valor_removido = conjunto.pop()
print(valor_removido)

# Limpando o conjunto
conjunto.clear()
print(conjunto)  # set()

# Conjuntos NÃO têm índice!
# Isso dá erro: conjunto[0]

# --------------------------
# OPERAÇÕES ENTRE CONJUNTOS
# --------------------------

a = {1, 2, 3}
b = {3, 4, 5}

# União (union ou |)
print(a | b)  # {1, 2, 3, 4, 5}
print(a.union(b))  # Mesmo resultado

# Interseção (elementos em comum)
print(a & b)  # {3}
print(a.intersection(b))

# Diferença (o que tem em A mas não em B)
print(a - b)  # {1, 2}
print(a.difference(b))

# Diferença simétrica (tudo menos os comuns)
print(a ^ b)  # {1, 2, 4, 5}
print(a.symmetric_difference(b))

# Subconjunto e superconjunto:
x = {1, 2}
y = {1, 2, 3}

print(x.issubset(y))  # True
print(y.issuperset(x))  # True

# Verificando se são disjuntos (sem interseção)
print(x.isdisjoint({3, 4}))  # True

# -------------------------
# COMPARAÇÕES ENTRE SETS
# -------------------------

# Dois conjuntos são iguais se tiverem os mesmos elementos
a = {1, 2, 3}
b = {3, 2, 1}
print(a == b)  # True

# --------------------------
# CONVERSÕES
# --------------------------

# De lista para conjunto
lista = [1, 2, 2, 3]
conjunto = set(lista)
print(conjunto)  # {1, 2, 3}

# De conjunto para lista
lista = list(conjunto)
print(lista)

# --------------------------
# SET COM STRINGS E TUPLAS
# --------------------------

# Strings são iteráveis, logo o set separa por caracteres únicos
print(set("banana"))  # {'b', 'n', 'a'}

# Tuplas funcionam como elementos de set (por serem imutáveis)
conjunto = {(1, 2), (3, 4)}
print((1, 2) in conjunto)  # True

# Listas não podem ser elementos de sets, pois são mutáveis
# Isso gera erro: set_with_list = {[1, 2], [3, 4]}

# ---------------------------
# SET COM COMPREHENSION
# ---------------------------

# Assim como listas e dicionários, também é possível criar conjuntos com comprehension
quadrados = {x ** 2 for x in range(5)}
print(quadrados)  # {0, 1, 4, 9, 16}

# ---------------------------
# EXEMPLO PRÁTICO: REMOVER DUPLICATAS
# ---------------------------

nomes = ["Ana", "Pedro", "Ana", "Lucas", "Pedro"]
nomes_unicos = list(set(nomes))
print(nomes_unicos)

# --------------------------
# CURIOSIDADES E DICAS
# --------------------------

# - Sets são muito rápidos para buscas: `x in set` é mais rápido que `x in list`
# - Sets são ótimos para eliminar duplicatas
# - Sets não garantem a ordem dos elementos
# - Sets só aceitam elementos **imutáveis**
# - Sets são iteráveis, mas não indexáveis

# --------------------------
# MINI SET (set de uma linha)
# --------------------------
if 2 in {1, 2, 3}: print("Está no conjunto")

# Evite construir sets com muitas operações em linha. Prefira clareza!
