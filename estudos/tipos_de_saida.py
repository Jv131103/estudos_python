# A função print() serve para exibir algo na tela. Pode receber vários argumentos,
# separados por vírgulas, e permite personalizar a saída com os parâmetros:
print("Olá", "mundo", sep=" - ", end="!\n")

# sep=" - " → separador entre os argumentos (Olá - mundo)
# end="!\n" → define o que vem no final (padrão é \n, quebra de linha)

# Formas de formatar strings em Python:

# Concatenação:
nome = "João"
print("Olá " + nome + "!")

# PS: Só pode concatenar strings. Se tiver número, precisa converter:
idade = 18
print("Idade: " + str(idade))

# Repetição de strings com *:
print("ha" * 3)  # "hahaha"

# % (Estilo antigo de formatação)
# %s → string
# %d → inteiro
# %f → float
# %.2f → float com 2 casas decimais

# Estilo antigo, ainda funciona, mas não é o mais recomendado hoje.
nome = "João"
idade = 18
print("Nome: %s | Idade: %d" % (nome, idade))

# .format() (Estilo intermediário)
nome = "João"
idade = 18
print("Nome: {} | Idade: {}".format(nome, idade))

# Também permite índices:
print("Idade de {0}: {1}".format(nome, idade))

# E nomeando os campos:
print("Nome: {n}, Idade: {i}".format(n=nome, i=idade))

# Também permite formatação:
pi = 3.14159
print("Valor de pi: {:.2f}".format(pi))  # 2 casas decimais

# f"" (f-strings, Python 3.6+)
# Forma mais moderna e clara! Permite inserir variáveis ou expressões diretamente dentro
# da string:
nome = "João"
idade = 18
print(f"Nome: {nome}, Idade: {idade}")

# Suporta expressões:
print(f"Idade daqui a 5 anos: {idade + 5}")

# Formatar número:
pi = 3.14159
print(f"Valor de pi: {pi:.2f}")

# Ajustar largura/alinhamento:
# PS: .format() e o % também fazem isso
print(f"{'Nome':<10} | {'Idade':>5}")  # Alinha à esquerda/direita
print(f"{nome:<10} | {idade:>5}")

# Quebra de linha em string:
print("Linha 1\nLinha 2")

# Tabulação:
print("Nome:\tJoão")

# Print com end e sep combinados:
print("Olá", end="... ")
print("tudo bem?")

# Escapando caracteres:
# \" ou \' → aspas dentro de strings
# \\ → barra invertida
# \n → nova linha
# \t → tabulação
print("Ele disse: \"Olá!\"")

# TAMBÉM PODEMOS FAZER O QUE CHAMAMOS DE interpolação de strings...
nome = "João"
mensagem = f"Olá {nome}"
print(mensagem)  # Funciona com .format() e também com %

# Uma forma de mirturar conceitos:
print(f"{'=' * 10} Bem-vindo, {nome} {'=' * 10}")
