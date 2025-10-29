# Tuplas são coleções ordenadas e imutáveis.
# Existem dois métodos para tuplas: count e index. Podemos criar tuplas com ()
# Também é possível concatenar tuplas, acessar índices e ver o tamanho dela

# Formas de definição
tupla1 = (1, 2, 3, 4, 5)
tupla2 = 1, 2, 3, 4, 5
tupla3 = ()  # Gera uma tupla vazia
print(tupla1, type(tupla1))
print(tupla2, type(tupla2))
print(tupla3, type(tupla3))

# ACESSANDO ÍNDICES
print(f"índice 0: {tupla1[0]}")
print(f"Ultimo indice: {tupla1[-1]}")  # Ou tupla1[len(lista)-1]
print(f"Ultimo indice negativo: {tupla1[-3]}")  # Ou tupla1[len(lista)-1]
print(f"Meio: {tupla1[len(tupla1) // 2]}")  # Ou tupla[2]

# Tamanho da tupla
# Inicia sempre de 1 elemento até N elementos
print(len(tupla1))

# Concatenação de tuplas, a única forma de unir tuplas
tupla3 = tupla1 + tupla2
print(tupla3)

# Fatiamento (Slicing)
# É bucar itens específicos em um intervalo em um iterável
# tupla[inicio:fim:intervalo]
# Pegando de 0 até 2
print(tupla3[:2])  # ltupla3sta[0:2]
# Pegando de 2 até 4
print(tupla3[2:4])
# Pegando de 2 até o último
print(tupla3[2:])  # tupla3[0:-1] ou tupla3[0:len(lista) - 1]
# Pegando de dois em dois
print(tupla3[::2])
# Pegando de trás para frente, ou seja, inverso.
print(tupla3[::-1])

# Empacotamento e desempacotamento de listas
# Empacotar é o mesmo que guardar itens dentro de um iterável mutável
# Desempacotar é remover qualquer itens dentro de iteráveis
valores = (350, 400, 900, 120)  # Isso pode ser o mesmo que enmpacotar
print(valores)
a, b, c, d = valores  # Isso é o mesmo que desempacotar
print(a, b, c, d)
# Se você quiser pegar só alguns valores e ignorar outros, ]
# usa _ (underline) para ignorar
primeiro, _, _, ultimo = valores
print(primeiro, ultimo)
# O * pega “o resto” dos valores e coloca em uma lista.
a, *b = valores
print(a)
print(b)
*a, b = valores
print(a)
print(b)
# Ambos ao mesmo tempo
a, b, *c = (1, 2, 3, 4, 5)
print(a, b, c)  # 1 2 [3, 4, 5]
x = (10, 20, 30)
y = (40, 50)
z = (*x, *y)  # junta listas
print(z)  # [10, 20, 30, 40, 50]

# Fazendo verificações na tupla
# Com in podemos ver se algo pertence a uma lista
# Com not in fazemos um inverso
k = ('F', 'M', 'J', 'K')
print('K' in k)
print('K' not in k)

# tuple é um construtor, ou seja, com ele, podemos definir valore como tupla
print(tuple([1, 2, 3, 4]))
print(tuple(range(0, 10)))

# Pegando o máximo
print(max(tupla3))

# Pegando o Mínimo
print(min(tupla3))

# soma
print(sum(tupla3))

# contar quantas vezes um item aparece na tupla
print(tupla3.count(5))

# Realizando busca da posição de um valor da tupla
print(tupla3.index(5))
# Buscando em posição específica
print(tupla3.index(5, 5))  # Posição 5 a diante, mas pode colocar final

# Inverter a tupla com reversed
print(list(reversed(tupla3)))

# Pegando indice e valor com enumerate
print(tuple(enumerate(tupla3)))

# Pegando valores de duas listas específicas e jogando em um só
t1 = (5, 10, 15, 25)
t2 = (30, 35, 40, 45, 50)  # Se um for maior, o zip ignorará o último
print(tuple(zip(t1, t2)))

# Podemo repetir elementos também:
ti = (0, 1)
ti *= 10  # Chama 0, 1 10 vezes
print(ti)

# Vai limpar a lista
del ti  # Se tentar chamar ou usar ela não vai mais existir
