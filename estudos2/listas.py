# Listas podem ser utilizadas para armazenar valores.
# Esses valores podem ser de qualquer tipo
# São mutáveis, ou seja, podem ser açlteradass ou substituídas

lista1 = [10, 20, 30, 40, 50]  # Lista de tipagem única
lista2 = ["Olá Mundo!", 10, 20, 30, [1, 2, 3], (45, 50)]  # Lista multi-valorada
lista3 = []  # Lista vazia

print(type(lista1))

# Acessando índices de uma lista
# Iniciam sempre de 0 até N-1 (N é o mesmo que o tamanho total da lista)
# Também podem iniciar de números negativos de -1 até -N
lista = ['A', 'B', 'C']
print(f"índice 0: {lista[0]}")
print(f"Ultimo indice: {lista[-1]}")  # Ou lista[len(lista)-1]
print(f"Ultimo indice negativo: {lista[-3]}")  # Ou lista[len(lista)-1]
print(f"Meio: {lista[len(lista) // 2]}")  # Ou lista[1]

# Tamanho da lista:
# Inicia sempre de 1 elemento até N elementos
print(len(lista))

# Modificando elementos de uma lista
# PS: Precisam corresponder com cada índice existente da lista
lista = [1, 2, 3]
print("Lista original:", lista)
# Modificando elementos diretamente (por índice)
# Cada posição (índice) pode ser alterada separadamente:
lista[0] = 10   # muda o primeiro elemento (índice 0)
lista[1] = 20   # muda o segundo
lista[2] = 30   # muda o terceiro
print("Após modificar por índice:", lista)
# Modificando elementos com uso de swap (troca de N elementos)
# Exemplo clássico de troca: primeiro ↔ último
temp = lista[0]       # guarda o primeiro valor
lista[0] = lista[-1]  # coloca o último no primeiro
lista[-1] = temp      # coloca o guardado no último
print("Após troca com temp:", lista)
# Isso serve para qualquer posição:
# Trocar o índice 1 com o índice 2
temp = lista[1]
lista[1] = lista[2]
lista[2] = temp
print("Após troca entre posições 1 e 2:", lista)
# Trocar valores diretamente (sem temp)
lista[0], lista[-1] = lista[-1], lista[0]
print("Após troca direta (sem temp):", lista)
# Copiar e modificar sem afetar a original
nova_lista = lista[::]  # Isso gera uma cópia original
nova_lista[0] = 999
print("Original:", lista)
print("Cópia modificada:", nova_lista)
# Se não gerar a cópia, a duas listas serão iguais e armazenadas no
# mesmo local de memória
nova_lista = lista  # Isso não sobrescreve, mas reatribui
nova_lista[0] = 999
print("Original:", lista)
print("Cópia modificada:", nova_lista)
# Swap com outra lista
a = [1, 2, 3]
b = [4, 5, 6]
a, b = b, a
print("a:", a, "b:", b)

# Fatiamento (Slicing)
# É bucar itens específicos em um intervalo em um iterável
# lista[inicio:fim:intervalo]
lista = [1, 2, 3, 4, 5]
# Pegando de 0 até 2
print(lista[:2])  # lista[0:2]
# Pegando de 2 até 4
print(lista[2:4])
# Pegando de 2 até o último
print(lista[2:])  # lista[0:-1] ou lista[0:len(lista) - 1]
# Pegando de dois em dois
print(lista[::2])
# Pegando de trás para frente, ou seja, inverso.
print(lista[::-1])
# Usando swap com slicing
lista[0:3], lista[3:5] = lista[3:5], lista[0:5]
print(lista)  # [4, 5, 4, 1, 2, 3, 4, 5]
# Swap parcial (mistura com slicing)
lista = [1, 2, 3, 4, 5]
lista[1:3], lista[3:5] = lista[3:5], lista[1:3]
print(lista)  # [1, 4, 5, 2, 3]

# list, index, máximo, mínimo, soma, count, reverse, .sort, sorted, zip, enumerate
# list é um construtor, ou seja, com ele, podemos definir valore como lista
valor = list()  # Gera uma lista vazia
print(list((1, 2, 3, 4)))

lista = [31, 914, 236, 376, 140, 705, 236]
# Realizando busca da posição de um valor da lista
print(lista.index(31))
# Buscando em posição específica
print(lista.index(236, 4))  # Posição 4 a diante, mas pode colocar final

# Pegando o máximo
print(max(lista))

# Pegando o Mínimo
print(min(lista))

# soma
print(sum(lista))

# contar quantas vezes um item aparece na lista
print(lista.count(236))

# Inverter a lista com reversed
print(list(reversed(lista)))

# Ordenar com .sort()
# PS: ele não pode ser atribuido, ele muda a lista por completo
lista.sort()
print(lista)
# Sequiser inverso
lista.sort(reverse=True)
print(lista)

# Ordenar com sorted
# PS: Ele pode ser atribuído, e assim pode não mudar o valor original da lista
lista = [31, 914, 236, 376, 140, 705, 236]
print(lista)
ordenada = sorted(lista)
print(ordenada)
# Sequiser inverso
ordenada = sorted(lista, reverse=True)
print(ordenada)

# Pegando indice e valor com enumerate
print(list(enumerate(lista)))

# Pegando valores de duas listas específicas e jogando em um só
l1 = [5, 10, 15, 25]
l2 = [30, 35, 40, 45, 50]  # Se um for maior, o zip ignorará o último
print(list(zip(l1, l2)))

# append e extend e insert
# append seta um valor para o último índice da lista,
# vantajoso por sempre atribuir na úktima posição
lista = ["João", "Maria", "Renato"]
lista.append("Giovanna")
print(lista)
# Se quisesse adicionar dois valores:
lista_n = [1, 2]
lista_n.append([3, 4])  # type: ignore  - Isso foi usado, para evitar erro typehint
print(lista_n)

# insert seta um valor em um campo específico, escolhedo um índice,
# Pode ser vantajoso em casos pequenos, ams em grades casos pode ser ruim,
# Por alterar as posições de cada valor na lista
lista.insert(2, "Melissa")
print(lista)

# extend "funde" duas listas em uma só, também podemos fazer isso com
# concatenação
lista_novo = ["Caio", "Alana", "Leandro", "Rodrigo", "Raquel"]
lista.extend(lista_novo)
print(lista)

lista_a_atribuir = ["Irineu", "Luana"]
lista += lista_a_atribuir
print(lista)

# Podemo repetir elementos também:
li = [0, 1]
li *= 10  # Chama 0, 1 10 vezes
print(li)

# pop, remove, del
# pop, vai remover o último elemento por padrão, mas vc pode definir um índice
# para remover também
lista.pop()
lista.pop(5)
print(lista)
# Também podemos atribuir o valor
pessoa_deletada = lista.pop()
print(pessoa_deletada)

# remove deleta um item específico da lista por meio de índice.
# Pode ser mais lento que o pop, devido a forma como o reverse é montado,
# Por que o reverse é focado em deletar o item, no caso o primeiro sempre,
# Já o pop, precisa de índice para remover
lista.remove("Raquel")
print(lista)

# Del remove tudo, até mesmo na memória
del lista[0]
print(lista)
# Vai limpar a lista
del lista  # Se tentar chamar ou usar ela não vai mais existir

# range(inicio, fim, intervalo): Cria um gerador que faz uma contagem
serie = list(range(2010, 2025))  # Cria uma lista de anos de 2010 até 2024
print(serie)

# Convertendo string em lista com split
frase = "Python é legal"
print(frase.split())  # Por padrão pega espaços, mas pode definir um valor
print(frase.split(" é "))

# Definindo listas em termos de variáveis
num1 = 10
num2 = 20
num3 = 30
lista = [num1, num2, num3]
print(lista)

# Empacotamento e desempacotamento de listas
# Empacotar é o mesmo que guardar itens dentro de um iterável mutável
# Desempacotar é remover qualquer itens dentro de iteráveis
valores = [350, 400, 900, 120]  # Isso pode ser o mesmo que enmpacotar
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
a, b, *c = [1, 2, 3, 4, 5]
print(a, b, c)  # 1 2 [3, 4, 5]
x = [10, 20, 30]
y = [40, 50]
z = [*x, *y]  # junta listas
print(z)  # [10, 20, 30, 40, 50]

# Fazendo verificações na lista
# Com in podemos ver se algo pertence a uma lista
# Com not in fazemos um inverso
k = ['F', 'M', 'J', 'K']
print('K' in k)
print('K' not in k)

# Fezendo cópia com copy
# PS: Isso é uma cópia parcial, ou seja, pode não copiar tudo dentro da lista
lista = [1, 2, 3]
lista_copia = lista.copy()
print(lista)
lista_copia[0] = 2
print(lista_copia)
