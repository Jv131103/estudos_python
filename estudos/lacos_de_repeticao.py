# ============================================================
# LAÇOS DE REPETIÇÃO EM PYTHON – for e while
# ============================================================

# Um laço (ou loop) é uma estrutura de repetição.
# Serve para executar um bloco de código várias vezes.

# Existem dois principais em Python:
#   for   – quando sabemos o número de repetições
#   while – quando não sabemos ao certo (depende de uma condição)

# ============================================================
# for – percorre sequências (strings, listas, tuplas, ranges...)
# ============================================================

# Exemplo com range:
for i in range(5):  # vai de 0 a 4
    print(i)

# range(start, stop, step) – você pode controlar tudo:
for i in range(1, 10, 2):  # de 1 até 9, pulando de 2 em 2
    print(i)

# Tradução:
# for --> para cada
# in   --> em
# range(5) --> intervalo de 0 a 4

# Exemplo com lista:
nomes = ["Ana", "João", "Carlos"]
for nome in nomes:
    print(nome)

# Exemplo com string:
for letra in "Python":
    print(letra)

# Enumerando índices:
for i, nome in enumerate(nomes):
    print(f"{i}: {nome}")

# Desempacotando tuplas:
dados = [("Ana", 20), ("João", 25)]
for nome, idade in dados:
    print(f"{nome} tem {idade} anos")

# ============================================================
# while – repete enquanto a condição for verdadeira
# ============================================================

# Exemplo básico:
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # cuidado com loops infinitos!

# Tradução:
# while --> enquanto

# Exemplo com entrada do usuário:
senha = ""
while senha != "python123":
    senha = input("Digite a senha: ")
print("Acesso liberado")

# ============================================================
# Controle de fluxo: break, continue e else no loop
# ============================================================

# break – encerra o loop imediatamente
for i in range(10):
    if i == 5:
        break
    print(i)

# Corrigido: usar o contador correto (não i) no while:
soma = 0
contador = 0
while contador < 10:
    if contador == 5:
        break
    soma += contador
    contador += 1
print(soma)

# continue – pula para a próxima iteração
for i in range(5):
    if i == 2:
        continue
    print(i)

string = "aeiou"
cont = 0
while cont < len(string):
    if string[cont] == "i":
        print("meio")
        cont += 1  # necessário para evitar loop infinito
        continue
    print(string[cont])
    cont += 1

# else – executado quando o loop termina naturalmente (sem break)
for i in range(5):
    print(i)
else:
    print("Loop concluído com sucesso!")

cont = 0
while cont < 5:
    print(cont)
    cont += 1
else:
    print("Loop concluído com sucesso!")

# ============================================================
# Laços aninhados (evite profundidade maior que 2-3 níveis)
# ============================================================

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

i = 0
while i < 3:
    j = 0  # precisa reiniciar j a cada volta
    while j < 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# ============================================================
# Laço com listas, strings, dicionários e sets
# ============================================================

# Dicionário:
dados = {"nome": "João", "idade": 30}
for chave in dados:
    print(chave, "=>", dados[chave])

# Com while:
chaves = list(dados)
i = 0
while i < len(chaves):
    print(chaves[i], "=>", dados[chaves[i]])
    i += 1

# Forma mais elegante:
for chave, valor in dados.items():
    print(f"{chave}: {valor}")

# Set (conjunto):
valores = {1, 2, 3}
for v in valores:
    print(v)

valores = {1, 2, 3}
while valores:
    print(valores.pop())  # remove e retorna um elemento arbitrário

# LISTAS

# Forma tradicional (while)
quadrados = []
i = 0
while i < 5:
    quadrados.append(i**2)
    i += 1
print(quadrados)

# Forma tradicional (for):
quadrados = []
for i in range(5):
    quadrados.append(i**2)
print(quadrados)

# Forma pythonica:
quadrados = [i**2 for i in range(5)]
print(quadrados)

# Também funciona com condicionais:
pares = [i for i in range(10) if i % 2 == 0]
print(pares)

# ============================================================
# Dicas e curiosidades:
# ============================================================

# while True – cria um loop infinito (use com cuidado!)
while True:
    print("Pressione Ctrl+C para sair")
    break  # normalmente quebramos com break

# range negativo:
for i in range(5, 0, -1):  # de 5 até 1
    print(i)

# Contagem negativa com while:
i = 10
while i >= 0:
    print(i)
    i -= 1

# Boas práticas:
# - Nome de variáveis de loop curtas: i, j, k (índices), item (elementos)
# - Evite alterar a lista que está sendo percorrida
# - Loops claros > loops complexos
# - Prefira for em coleções conhecidas, while para condições abertas

# ============================================================
# VARIÁVEIS CONTADORAS E ACUMULADORAS
# ============================================================

# 🔢 Contador: serve para contar quantas vezes algo ocorreu.
# ➕ Acumulador: serve para somar valores ao longo do loop.
#   Contador: contador += 1
#   Acumulador: acumulador += valor

# ------------------------------------------------------------
# EXEMPLOS COM for
# ------------------------------------------------------------

# Contador: quantos números pares existem de 1 a 10?
contador = 0
for i in range(1, 11):
    if i % 2 == 0:
        contador += 1
print(f"Total de pares: {contador}")

# Acumulador: soma de todos os números de 1 a 5
soma = 0
for i in range(1, 6):
    soma += i
print(f"Soma total: {soma}")

# Contador e acumulador juntos:
notas = [7, 8.5, 6, 9]
soma = 0
contador = 0
for nota in notas:
    soma += nota
    contador += 1
media = soma / contador
print(f"Média: {media:.2f}")

# ------------------------------------------------------------
# EXEMPLOS COM while
# ------------------------------------------------------------

# Contador: contar quantas vezes o loop roda
contador = 0
i = 1
while i <= 10:
    contador += 1
    i += 1
print(f"Loop rodou {contador} vezes")

# Acumulador: somar valores digitados pelo usuário
soma = 0
entrada = ""
while entrada != "sair":
    entrada = input("Digite um número ou 'sair': ")
    if entrada != "sair":
        soma += int(entrada)
print(f"Soma total: {soma}")

# Contador e acumulador com verificação de valores válidos
soma = 0
contador = 0
while True:
    entrada = input("Digite uma nota (ou 'fim'): ")
    if entrada.lower() == "fim":
        break
    nota = float(entrada)
    if 0 <= nota <= 10:
        soma += nota
        contador += 1
    else:
        print("Nota inválida")
if contador > 0:
    media = soma / contador
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota válida foi digitada")
