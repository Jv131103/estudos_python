# Tupla em Python
# Uma tupla é uma estrutura de dados imutável. Ela serve para armazenar
# uma sequência de valores que não devem ser alterados.
# "Imutável" significa que, após criada, você não pode alterar seus valores.

# Tradução:
# Tupla (tuple) --> saco de valores que você NÃO PODE mexer

# Tuplas são muito úteis quando:
# - Você quer proteger os dados
# - Precisa usar como chave de dicionário (pois são hasháveis)
# - Precisa retornar múltiplos valores de uma função
# - Deseja economizar memória (tuplas são menores que listas)

# Como criar uma tupla:
tupla1 = (1, 2, 3)  # Tupla de 3 elementos
tupla2 = "a", "b", "c"  # Também é tupla! Parênteses são opcionais
tupla3 = ()  # Tupla vazia
tupla4 = (42,)  # Tupla de um elemento -> precisa da vírgula!

# ATENÇÃO:
# Sem a vírgula, não é tupla!
nao_tupla = (42)
print(type(nao_tupla))  # <class 'int'>

# Tupla pode conter qualquer tipo:
tupla5 = (1, "texto", True, [1, 2], (9, 8))

# Acessando elementos:
print(tupla1[0])  # 1
print(tupla1[-1])  # 3

# Fatiamento (slicing)
print(tupla1[1:])  # (2, 3)

# Métodos disponíveis (poucos, por ser imutável):
print(tupla1.count(2))  # Conta quantas vezes aparece
print(tupla1.index(3))  # Retorna o índice da primeira ocorrência

# Desempacotamento:
x, y, z = tupla1
print(x, y, z)

# Pode usar "_" para ignorar valores:
a, _, c = (10, 20, 30)
print(a, c)

# Pode usar * para pegar o resto:
primeiro, *meio, ultimo = (1, 2, 3, 4, 5)
print(meio)  # [2, 3, 4]

# Tuplas são imutáveis!
# tupla1[0] = 99  # Erro! TypeError

# Mas cuidado: se tiver objetos mutáveis dentro, esses podem mudar!
tupla_mutavel = ([1, 2, 3],)
tupla_mutavel[0].append(4)
print(tupla_mutavel)  # ([1, 2, 3, 4],)

# Verificação de existência:
if 2 in tupla1:
    print("Tem 2")

# Iteração:
for valor in tupla2:
    print(valor)


# Pode ser usada como retorno de múltiplos valores:
def operacoes(a, b):
    return a + b, a - b, a * b


soma, sub, mult = operacoes(4, 2)
print(soma, sub, mult)

# Tuplas podem ser concatenadas:
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 4)

# Repetição:
print(t1 * 3)  # (1, 2, 1, 2, 1, 2)

# Comprimento:
print(len(t1))  # 2

# Tuplas aninhadas (matrizes):
matriz = (
    (1, 2),
    (3, 4)
)
print(matriz[1][0])  # 3

# Convertemos lista para tupla:
lista = [1, 2, 3]
tupla = tuple(lista)

# E vice-versa:
nova_lista = list(tupla)

# Tuplas como chaves de dicionário:
localidades = {
    (23.5, 45.1): "Ponto A",
    (12.4, 32.1): "Ponto B"
}

# Sorted com tuplas:
tuplas = [(3, "c"), (1, "a"), (2, "b")]
print(sorted(tuplas))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# É possível usar tuplas para múltiplos retornos, chave composta, imutabilidade segura...

# Boas práticas com tuplas:
# 1. Use tuplas para dados que não devem mudar
# 2. Prefira tuplas a listas quando possível (eficiência e segurança)
# 3. Se precisar nomear os campos, use namedtuple ou dataclass

# Exemplo com namedtuple:
from collections import namedtuple

Pessoa = namedtuple("Pessoa", "nome idade")
p = Pessoa("João", 30)
print(p.nome, p.idade)

# Armadilhas:
# 1. Tupla de um único elemento precisa da vírgula
# 2. Tuplas com objetos mutáveis ainda podem ser "modificadas por dentro"
# 3. IndexError se tentar acessar índice inválido

# Curiosidade:
# Tuplas são mais leves na memória que listas:
import sys

print(sys.getsizeof([1, 2, 3]))  # Lista
print(sys.getsizeof((1, 2, 3)))  # Tupla

# Também são mais rápidas em acesso e criação (porque são imutáveis)

# Tupla vs Lista:
# Lista = usa quando precisa alterar
# Tupla = usa quando não precisa alterar

# Por fim, lembrar:
# Tupla é simples, rápida, segura e poderosa — como uma pedrinha ninja
