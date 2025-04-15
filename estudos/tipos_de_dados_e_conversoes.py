# TIPOS DE DADOS EM PYTHON E CONVERSÕES

# Em Python, tudo é um OBJETO. Cada valor tem um tipo associado a ele,
# e todo tipo tem métodos e comportamentos específicos.

# --- PRINCIPAIS TIPOS PRIMITIVOS ---

# int     → números inteiros (ex: 1, -3, 42)
# float   → números com ponto flutuante (ex: 3.14, -0.5)
# str     → textos (ex: "João", "123")
# bool    → valores lógicos (True ou False)
# complex → números complexos (ex: 2 + 3j)
# None    → tipo especial que representa "nada" (ausência de valor)

# --- VERIFICANDO O TIPO DE UM VALOR ---
x = 10
print(type(x))             # <class 'int'>
print(isinstance(x, int))  # True

# --- CONVERSÕES ENTRE TIPOS (CASTING) ---

# STRING → INTEIRO
texto = "1"
numero = int(texto)
print(numero, type(numero))  # 1 <class 'int'>

# STRING → FLOAT
texto = "3.14"
numero = float(texto)
print(numero, type(numero))  # 3.14 <class 'float'>

# INTEIRO → STRING
num = 42
texto = str(num)
print(texto, type(texto))  # "42" <class 'str'>

# FLOAT → STRING
pi = 3.1415
texto = str(pi)
print(texto, type(texto))  # "3.1415" <class 'str'>

# BOOLEANO → INTEIRO
print(int(True))   # 1
print(int(False))  # 0

# INTEIRO → BOOLEANO
print(bool(1))     # True
print(bool(0))     # False
print(bool(42))    # True

# STRING → BOOLEANO
print(bool(""))      # False
print(bool("abc"))   # True

# FLOAT → INTEIRO (trunca o valor, não arredonda)
n = 3.99
print(int(n))  # 3

# FLOAT COM VÍRGULA (precisa trocar vírgula por ponto)
texto = "3,14".replace(",", ".")
print(float(texto))  # 3.14

# PS: podemos deifini inputs vazios com essas formatações de entrada
# EX:
x = int(input())  # Aqui definimos um input vazio que vai pedir um número
print(x)

# --- ATENÇÃO! ---
# Nem toda conversão é possível!
# texto = "abc"
# int(texto)  # Vai gerar erro: ValueError

# --- NÚMEROS BINÁRIOS, OCTAIS E HEXADECIMAIS ---

num = 42
print(bin(num))   # '0b101010' → binário
print(oct(num))   # '0o52'     → octal
print(hex(num))   # '0x2a'     → hexadecimal

# Podemos converter de volta usando int com base:
print(int("101010", 2))  # 42 (binário → inteiro)
print(int("2a", 16))     # 42 (hexadecimal → inteiro)

# --- CONVERSÕES UNICODE/ASCII ---
# Unicode e ASCII são padrões de codificação de caracteres, ou seja, eles definem uma maneira
# de representar caracteres (como letras, números, símbolos) em números, permitindo que
# computadores e sistemas os entendam e os processem.
# Caso queiram analisar as tabelas, acessem os arquivos unicode.py e ascii.py

print(ord("A"))  # 65  → código numérico da letra
print(chr(66))   # 'B' → caractere correspondente

# Codificando e decodificando conversões
texto = "Olá"
bytes_texto = texto.encode('utf-8')  # Codificação para bytes
print(bytes_texto)  # b'Ol\xc3\xa1'
texto_decodificado = bytes_texto.decode('utf-8')  # Decodificação para bytes
print(texto_decodificado)  # Olá

# --- TIPO NONE (ausência de valor) ---
# O None em Python é um tipo de dado especial que é utilizado para representar
# a ausência de valor ou a falta de valor definido. Ele é um objeto único da
# classe NoneType. O None pode ser atribuído a uma variável para indicar que
# ela não possui um valor significativo ou que não foi inicializada corretamente.
nada = None
print(nada, type(nada))  # None <class 'NoneType'>

# --- NÚMEROS COMPLEXOS ---
z = 2 + 3j
print(z, type(z))        # (2+3j) <class 'complex'>
print(z.real)            # Parte real: 2.0
print(z.imag)            # Parte imaginária: 3.0

# --- MÉTODOS DE STRINGS PARA VERIFICAÇÃO ---

s = "123"
print(s.isdigit())    # True → Só tem dígitos?
print(s.isdecimal())  # True → Só aceita números 0 a 9
print(s.isnumeric())  # True → Números, incluindo romanos (ex: 'Ⅷ')

s = "abc"
print(s.isalpha())    # True → Só letras?

s = "abc123"
print(s.isalnum())    # True → Letras e/ou números

s = "   "
print(s.isspace())    # True → Só espaços?

s = "Python"
print(s.islower())    # False
print(s.isupper())    # False
print(s.istitle())    # True

print("python".islower())     # True
print("ABC".isupper())        # True
print("Olá Mundo".istitle())  # True

print("abc".isascii())             # True → Só caracteres ASCII
print("nome_da_var".isidentifier())  # True → Pode ser usado como nome de variável?
print("Olá mundo!".isprintable())    # True → Todos os caracteres podem ser impressos?

# --- EXPLORANDO OS OBJETOS E MÉTODOS ---
print(dir("abc"))  # Mostra todos os métodos e atributos disponíveis

# --- AVALIAÇÃO DE EXPRESSÕES COM STRING (com cuidado!) ---
valor = eval("3 + 4")
print(valor)  # 7

# ATENÇÃO: Nunca use eval() com dados de usuário sem segurança. Pode ser perigoso!

# --- EXEMPLO DE CONVERSÃO SEGURA COM TRATAMENTO DE ERROS ---
# PS: Vamos analisar isso em tratamento_erros.py
texto = "abc"
try:
    numero = int(texto)
except ValueError:
    print("Não é possível converter para inteiro.")
