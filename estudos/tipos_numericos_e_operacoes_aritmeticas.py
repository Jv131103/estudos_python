# Em Python, temos três tipos básicos para representar números:

# int - – Inteiros
# Números sem parte decimal: 0, -10, 42, 999999
numero = 10
b = -42
c = 10**100  # Python suporta inteiros muito grandes
print(type(numero))  # <class 'int'>

# float – Ponto flutuante (decimais)
# Usa ponto . como separador decimal: 3.14, -0.5, 2.0
numero = 3.14
neg = -0.5
zero = 0.0
print(type(numero))  # <class 'float'>

# complex – Números complexos
# Com parte real e imaginária: 1 + 2j
z = 1 + 2j
print(type(z))  # <class 'complex'>
print(z.real, z.imag)  # 1.0 2.0

# Também temos os tipos bin(Binário), oct(Octal) e hex(Hexadecimal)
bin(10)   # '0b1010'
oct(10)   # '0o12'
hex(10)   # '0xa'
int('0b1010', 2)  # 10 (converte binário pra decimal)
print(int('0xff', 16))   # 255 (de hexadecimal pra decimal)

# OPERAÇÕES ARITMÉTICAS BÁSICAS:
# Operação	        Símbolo	    Exemplo	Resultado
# Adição	        +	        3 + 2	5
# Subtração	        -	        5 - 2	3
# Multiplicação	    *	        4 * 3	12
# Divisão	        /	        7 / 2	3.5 (sempre float)
# Divisão inteira	//	        7 // 2	3 (parte inteira)
# Módulo	        %	        7 % 2	1 (resto da divisão)
# Potência	        **	        2 ** 3	8
# Negativo	        -	        -5	-5
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(2 % 2)
print(2 // 2)
print(2**2)
print(-2)

# Operações mistas e precedência
# Ordem de precedência (ordem que o Python executa):
# () – Parênteses
# ** – Potência
# * / // % – Multiplicação, divisão, etc.
#   + - – Soma e subtração

resultado = 3 + 4 * 2 ** 2  # 3 + 4 * 4 → 3 + 16 → 19
print(resultado)

x = 2 + 3 * 4  # 2 + 12 = 14
print(x)

y = (2 + 3) * 4  # 5 * 4 = 20
print(y)

# Podemos referenciar e gerar fórmulas cálculos

# Conversões:
# Você pode converter entre os tipos:
int(3.9)      # 3
float(10)     # 10.0
complex(3)    # (3+0j)

# Funções matemáticas úteis:
import math

print(math.sqrt(16))      # raiz quadrada: 4.0
print(math.pow(2, 3))     # potência: 8.0
print(math.pi)            # 3.14159...
print(math.floor(3.9))    # arredonda pra baixo: 3
print(math.ceil(3.1))     # arredonda pra cima: 4
print(math.trunc(3.9))    # trunca (remove decimal): 3

# Operações com sinais:
print(abs(-5))      # 5 (valor absoluto)
print(-abs(5))      # -5

# Arredondamentos:
round(3.456, 2)  # 3.46 → arredonda com 2 casas decimais
round(3.5)       # 4
round(2.5)       # 2 (regra do round "para o par mais próximo")

# Imprecisoes de ponto flutuante
# Os computadores armazenam números em binário (base 2).

# Alguns números que são simples em decimal (base 10), como 0.1, não têm uma representação
# exata em binário.

# Então o Python (e o processador) arredonda o valor para o mais próximo possível —
# mas não é exato.
print(0.1 + 0.2)  # 0.30000000000000004 ← imprecisão binária
print(0.3 == 0.1 + 0.2)  # False!
print(1.1 + 2.2 == 3.3)  # False também!

# limite de números inteiros, floates e complex
# int: Em Python, não há limite fixo de tamanho (só pela memória).
# float:
#   Baseado no padrão IEEE 754.
#   Máximo: 1.7976931348623157e+308
#   Mínimo positivo: 5e-324
# complex: Limitado pelos limites de float (real e imaginária).
import sys

print(sys.float_info)

# O problema de realizar grandes cálculos:
calculo = 90**10000

# O Python realiza o cálculo com sucesso, mesmo sendo gigantesco, porque o tipo int
# em Python é ilimitado em tamanho, limitado apenas pela memória disponível do sistema.
# Isso é uma grande vantagem do Python em relação a outras linguagens como C/C++ ou Java,
# que têm limites fixos (ex: int32, int64).

# print(calculo)

# Mas qual é o problema então?

# Consumo de memória: Um número enorme como 90**10000 pode ocupar centenas de megabytes ou
# até gigabytes só para armazenar esse único valor.

# Tempo de processamento: Leva tempo para o Python calcular e depois converter esse número
# em string para exibir no print(). Isso pode congelar o terminal ou travar o programa em
# sistemas mais fracos.

# Impressão e visualização: Vai imprimir milhares de dígitos, o que torna inviável de ler ou
# usar na prática
