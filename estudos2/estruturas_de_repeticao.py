# estruturas de repetição permitem executar um bloco várias vezes
# controlando quantas vezes e quando parar.

# ESTRUTURAS:
# while <condição>:
#     <bloco>      # executa enquanto a condição for verdadeira
#
# for <variável> in <iterável>:
#     <bloco>      # executa para cada item do iterável

print("=== 1) while básico: contador manual ===")
# incrementador (i += 1), contador e acumulador
i = 1               # contador (quantas vezes)
soma = 0            # acumulador (soma de valores)
while i <= 5:
    soma += i       # acumulador recebe o valor atual
    print("i =", i, "| soma =", soma)
    i += 1          # incrementador (passo)
print("Total soma 1..5 =", soma)
print("Seguindo\n")


print("=== 2) for com range (início, fim, passo) ===")
# range(fin) -> 0..fin-1
# range(inicio, fim[, passo])
for n in range(1, 6):  # 1..5
    print(n, end=" ")
print("\nCom passo 2:", list(range(0, 10, 2)))
print("Seguindo\n")


print("=== 3) break, continue e for-else ===")
# break: sai do laço
# continue: pula para a próxima iteração
# for-else: o 'else' roda se o laço NÃO for interrompido por break
nums = [1, 3, 5, 8, 11, 14]
alvo_par = None
for v in nums:
    if v % 2 == 0:
        alvo_par = v
        print("Primeiro par encontrado:", v)
        break
else:
    print("Nenhum número par encontrado")
print("continue (pular ímpares):", end=" ")
for v in nums:
    if v % 2 != 0:
        continue
    print(v, end=" ")
print("\nSeguindo\n")


print("=== 4) contador de ocorrências (contagem) ===")
# contar quantas vezes um valor aparece
letras = list("banana")
contador_a = 0
for ch in letras:
    if ch == "a":
        contador_a += 1
print("Quantidade de 'a' em 'banana':", contador_a)
print("Seguindo\n")


print("=== 5) iterando coleções (lista, tupla, set, dict) ===")
lista = [10, 20, 30]
tupla = (1, 2, 3)
conjunto = {3, 3, 2, 1}  # set remove duplicatas
dicionario = {"nome": "Ana", "idade": 22}

print("lista:", end=" ")
for x in lista:
    print(x, end=" ")
print("\ntupla:", end=" ")
for x in tupla:
    print(x, end=" ")
print("\nset (ordem não garantida):", end=" ")
for x in conjunto:
    print(x, end=" ")
print("\nkeys dict:", list(dicionario.keys()))
print("values dict:", list(dicionario.values()))
print("items dict (chave, valor):", end=" ")
for k, v in dicionario.items():
    print(f"({k}={v})", end=" ")
print("\nSeguindo\n")


print("=== 6) enumerate (índice + valor) e zip (sincronizar listas) ===")
frutas = ["maçã", "banana", "uva"]
precos = [3.5, 4.2, 6.0]
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}. {fruta}")
print("zip (fruta + preço):")
for fruta, preco in zip(frutas, precos):
    print(f"{fruta}: R$ {preco:.2f}")
print("Seguindo\n")


print("=== 7) swap (troca) com variáveis e com listas usando laço ===")
# swap de variáveis (pythônico):
a, b = 10, 99
print("Antes swap variáveis:", a, b)
a, b = b, a
print("Depois swap variáveis:", a, b)

print("Fazendo swap simples dentro de um laço")
n1 = 0
n2 = 1
while n2 < 10:
    print(n2, end=" ")
    temp = n1
    n1 = n2
    n2 = n2 + temp
print()


# swap em lista: inverter in-place com dois ponteiros
nums = [1, 2, 3, 4, 5]
i, j = 0, len(nums) - 1
while i < j:
    nums[i], nums[j] = nums[j], nums[i]   # swap de elementos
    i += 1
    j -= 1
print("Lista invertida com laço:", nums)
print("Seguindo\n")


print("=== 8) iteradores: iter(), next() e StopIteration ===")
dados = [100, 200, 300]
it = iter(dados)                # obtém um iterador
print(next(it))                 # 100
print(next(it))                 # 200
print(next(it))                 # 300
try:
    print(next(it))            # levanta StopIteration
except StopIteration:
    print("Iterador esgotado (StopIteration)")
print("Seguindo\n")


print("=== 9) geradores (yield): criam iteradores fáceis ===")


# gerador produz valores sob demanda, economizando memória
def pares_ate(n):
    atual = 0
    while atual <= n:
        if atual % 2 == 0:
            yield atual
        atual += 1


for p in pares_ate(10):
    print(p, end=" ")
print("\nSeguindo\n")


print("=== 10) laço com sentinela (while True + break) ===")
# padrão útil quando não sabemos a quantidade de repetições de antemão
# (ex: leitura de arquivo, entrada do usuário etc.)
contador = 0
while True:
    contador += 1
    if contador >= 3:
        print("Pare aqui (break). contador =", contador)
        break
print("Seguindo\n")


print("=== 11) compreensões: forma declarativa de repetir ===")
# list/set/dict comprehensions resumem laços simples
quadrados = [x * x for x in range(6)]           # lista
pares = {x for x in range(10) if x % 2 == 0}    # set
mapa = {ch: ord(ch) for ch in "abc"}            # dict
print("quadrados:", quadrados)
print("pares:", pares)
print("mapa:", mapa)
print("Seguindo\n")


print("=== 12) boas práticas para evitar 'hadouken indentation' em laços ===")
# Use 'continue' para pular cedo e manter o laço plano
valores = [0, -1, 3, -2, 5]
positivos = []
for v in valores:
    if v <= 0:
        continue  # pula negativos e zero
    positivos.append(v)
print("Só positivos:", positivos)

# loops aninhados. loops embaixo de loops
print("=== 13) laços aninhados (for dentro de for, while dentro de while) ===")
# 13.1) Tabuada (for-for)
print("\nTabuada 1..3:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("-- fim da linha --")

# 13.2) Matriz: impressão em grade (for-for)
print("\nMatriz 3x3:")
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j], end=" ")
    print()

# 13.3) Soma de todos os elementos (for-for)
soma_total = 0
for linha in mat:
    for valor in linha:
        soma_total += valor
print("\nSoma total da matriz:", soma_total)

# 13.4) Padrão/Desenho (while-while)
print("\nTriângulo de asteriscos (while-while):")
lin = 1
while lin <= 4:
    col = 1
    while col <= lin:
        print("*", end="")
        col += 1
    print()
    lin += 1

# 13.5) Busca com early-break em laços aninhados
print("\nBusca por valor 5 na matriz (com break duplo):")
encontrou = False
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 5:
            print(f"Achou 5 em (i={i}, j={j})")
            encontrou = True
            break  # sai do laço interno
    if encontrou:
        break      # sai do laço externo

# 13.6) Produto cartesiano (for-for) vs itertools.product
print("\nProduto cartesiano (A x B):")
A = ["a", "b"]
B = [1, 2, 3]
pares = []
for x in A:
    for y in B:
        pares.append((x, y))
print("pares:", pares)

# 13.7) Flatten (achatar) lista de listas (for aninhado)
print("\nFlatten de lista de listas:")
lista_de_listas = [[1, 2], [3, 4], [5]]
flat = []
for sub in lista_de_listas:
    for item in sub:
        flat.append(item)
print("flat:", flat)

# 13.8) Compreensão com dois fors (equivalente ao flatten acima)
flat2 = [item for sub in lista_de_listas for item in sub]
print("flat (compreensão):", flat2)

# 13.9) Filtro duplo com laços aninhados (somente pares em 1..5 x 1..5)
print("\nPares em 1..5 x 1..5:")
pares_xy = []
for x in range(1, 6):
    for y in range(1, 6):
        if (x * y) % 2 == 0:
            pares_xy.append((x, y))
print(pares_xy)

# 13.10) while-for (misto)
print("\nMisto while-for:")
k = 2
while k <= 10:
    linha = []
    for j in range(1, 11):
        linha.append(k * j)
    print(f"k={k} ->", linha)
    k += 1

print("\nObservação: laços aninhados costumam ser O(n^2). Evite profundidade desnecessária.")


print("Fim.")
