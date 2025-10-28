# Comparação: (==, !=, >=, <=, >, <)
print("Igual (==):", 10 == 10)
print("Diferença (!=):", 10 != 10)
print("Maior ou igual (>=):", 10 >= 10)
print("Maior ou igual (>=) com strings:", 'a' >= 'A')
print("Menor ou igual (<=):", 10 <= 5)
print("Menor ou igual (<=) com strings:", 'x' <= 'A')
print("Maior (>):", 10 > 10)
print("Maior (>) com strings:", 'a' > 'A')
print("Menor (<):", 10 < 5)
print("Menor (<) com strings:", 'x' < 'A')

# Lógico (and, or, not)
print("AND: Apenas será verdade se ambas as afirmações forem True")
print(20 > 2 and 10 > 2)
print(20 > 2 and 2 > 10)
# Curto-circuito, ou seja, para na primeira afirmação falsa para and
print(2 > 20 and 2 > 10)
print("Tabela verdade (AND)")
print(f"V and V = {True and True}")
print(f"V and F = {True and False}")
print(f"F and V = {False and True}")
print(f"F and F = {False and False}")
print("OR: Apenas será False se ambas as afirmações forem falsas")
print(2 > 20 or 2 < 10)
print(2 > 20 or 2 > 10)
# Curto-circuito, ou seja, se for verdade, ele para na primeira afirmação
print(2 < 10 or 2 < 20)
print("Tabela verdade (OR)")
print(f"V or V = {True or True}")
print(f"V or F = {True or False}")
print(f"F or V = {False or True}")
print(f"F or F = {False or False}")
print("NOT: É a negação de qualquer afirmação")
print("Verdade - Falso")
print("Falso - Verdade")
print(not 1)  # 1 representa True (ligado) - Negação será False
print(not 0)  # 0 representa False (desligado) - Negação será True
print("Tabela verdade (NOT)")
print(f"V = {not True}")
print(f"F = {not False}")

# Para qualquer iterável, é possível utilizar not para validar o inverso
# de sua afirmação
valor = [1, 2, 3]
print(1 not in valor)
print(1 in valor)
texto = "Olá Mundo"
print("Ola" not in texto)

# Bit-wise
# São operações feitas bit a bit (nível binário) nos números inteiros.
a = 5  # 0101 em binário
b = 3  # 0011 em binário
# AND = &
print(a & b)  # 1
# OR = |
print(a | b)  # 7
# XOR (Também chamado de OU OU) = ^
print(a ^ b)  # 6
# NOT = ~
print(~a)     # -6
# Shift left (desloca à esquerda)
print(a << 2)  # 20 (0101 -> 10100)
# Shift right (desloca à direita)
print(a >> 1)  # 2  (0101 -> 0010)

# Atribuição (=, +=, -=, /=, //=, %=, **=):
# Atribuição simples
x = 10      # O valor 10 é armazenado em x
print("x =", x)
# Adição e atribuição
x += 5      # x = x + 5 → soma 5 ao valor atual de x
print("x += 5 →", x)
# Subtração e atribuição
x -= 3      # x = x - 3 → subtrai 3 do valor atual de x
print("x -= 3 →", x)
# Divisão e atribuição
x /= 2      # x = x / 2 → divide x por 2 (resultado float)
print("x /= 2 →", x)
# Divisão inteira e atribuição
x //= 2     # x = x // 2 → divide por 2 e pega só a parte inteira
print("x //= 2 →", x)
# Módulo e atribuição
x %= 3      # x = x % 3 → pega o resto da divisão por 3
print("x %= 3 →", x)
# Potenciação e atribuição
x **= 4     # x = x ** 4 → eleva o valor atual de x à quarta potência
print("x **= 4 →", x)

# Atribuição bit-wise
a = 5  # 0101
b = 3  # 0011

# AND e atribui
a &= b  # É o mesmo que: a = a & b
print(a)
# OR e atribui
a = 5
a |= b   # É o mesmo que: a = a | b
print(a)
# XOR e atribui
a = 5
a ^= b  # É o mesmo que: a = a ^ b
print(a)
# Desloca à esquerda e atribui
a = 5
a <<= 1  # É o mesmo que: a = a << 1
print(a)
# Desloca à direita e atribui
a = 5
a >>= 1  # É o mesmo que: a = a >> 1
print(a)
