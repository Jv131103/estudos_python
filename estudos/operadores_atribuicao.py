# Operadores de Atribuição
# São usados para atribuir valores a variáveis.
# O mais comum é o = (igual simples), mas há vários compostos que fazem
# operação e atribuição de uma vez.

# PS: Isso será muito útil, em situações em que usaamos laços no Python

# Operador	    Significado	    Exemplo	    Equivalente a
#   =	    Atribuição simples	 a = 5	         —
# Compostos (operam e atribuem):
# Operador	   Significado	        Exemplo	    Equivalente a
#   +=	    Soma e atribuição	    a += 1	       a = a + 1
#   -=	   Subtração e atribuição	a -= 2	       a = a - 2
#   *=	      Multiplicação	        a *= 3	       a = a * 3
#   /=	      Divisão (float)	    a /= 2	       a = a / 2
#   //= 	  Divisão inteira	    a //= 2	       a = a // 2
#   %=	         Módulo	            a %= 3	       a = a % 3
#   **=	      Exponenciação	        a **= 2	       a = a ** 2
#   &=	       E bit a bit	        a &= 1	       a = a & 1
#   |=	       OU bit a bit	        a |= 1         a = a | 1
#   ^=	      XOR bit a bit	        a ^= 1	       a = a ^ 1
#   >>=	     Desloca à direita	    a >>= 2	       a = a >> 2
#   <<=	     Desloca à esquerda	    a <<= 2	       a = a << 2

# Atribuição simples
x = 10
print("x =", x)  # 10

# Soma e atribuição
x += 3  # x = x + 3
print("x += 3 →", x)  # 13

# Subtração e atribuição
x -= 5  # x = x - 5
print("x -= 5 →", x)  # 8

# Multiplicação e atribuição
x *= 2  # x = x * 2
print("x *= 2 →", x)  # 16

# Divisão float e atribuição
x /= 4  # x = x / 4
print("x /= 4 →", x)  # 4.0 (vira float!)

# Divisão inteira e atribuição
x //= 2  # x = x // 2
print("x //= 2 →", x)  # 2.0

# Módulo e atribuição
x %= 2  # x = x % 2
print("x %= 2 →", x)  # 0.0

# Exponenciação e atribuição
x = 3
x **= 3  # x = x ** 3
print("x = 3 → x **= 3 →", x)  # 27

# Bitwise AND e atribuição
x = 6       # bin: 110
x &= 3      # x = x & 3 → 110 & 011 = 010
print("x = 6 → x &= 3 →", x)  # 2

# Bitwise OR e atribuição
x |= 4      # x = x | 4 → 010 | 100 = 110
print("x |= 4 →", x)  # 6

# Bitwise XOR e atribuição
x ^= 5      # x = x ^ 5 → 110 ^ 101 = 011
print("x ^= 5 →", x)  # 3

# Bitwise deslocamento para a direita
x >>= 1     # x = x >> 1 (divide por 2 e arredonda pra baixo)
print("x >>= 1 →", x)  # 1

# Bitwise deslocamento para a esquerda
x <<= 4     # x = x << 4 (multiplica por 2^4 = 16)
print("x <<= 4 →", x)  # 16
