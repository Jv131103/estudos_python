# Em Python, o tipo Booleano (bool) é usado para representar valores lógicos:
#   True → verdadeiro
#   False → falso

# Eles são usados em condições, comparações, validações, filtros, etc.
a = True
b = False

print(type(a))  # <class 'bool'>

# Podemos também definir variáveis de opção ou de execução:
nome = input("Digite seu nome: ") or "Anônimo"

modo_debug = False
modo_teste = True

modo_ativo = modo_debug or modo_teste
print("Modo ativo:", modo_ativo)

x = 'olá' and 'mundo'
print(x)  # 'mundo' (ambos são "True")

x = '' and 'mundo'
print(x)  # '' (string vazia é False)

idade = 18
eh_de_maior = idade >= 18  # Valida e já retorna o boolean correspondente
print(eh_de_maior)  # True

# Operações que retornam Booleanos:
# Comparações:
# Operadores de Comparação:
# ===============================================================================
# Operador	      Significado	    Exemplo	            Resultado
# ===============================================================================
#   ==	             Igual	        5 == 5	            True
#   !=	           Diferente	    5 != 3	            True
#   >	           Maior que	    4 > 2	            True
#   <	           Menor que	    3 < 5	            True
#   >=	        Maior ou igual	    5 >= 5	            True
#   <=	        Menor ou igual	    4 <= 3	            False
#   is	   Igualdade de identidade	a is b	            True se mesmo objeto
# is not   Diferença de identidade	a is not b	        True se objetos distintos
#   in	            Pertence	    'a' in 'abc'	    True
# not in	      Não pertence	    'z' not in 'abc'	True
# ===============================================================================
# Todas essas operações retornam True ou False:
print(5 == 5)     # True
print(5 != 3)     # True
print(7 > 2)      # True
print(4 >= 4)     # True
print(3 < 2)      # False

# Operador de identidade: Veja mais em listas.py
x = [1, 2]
y = x
z = [1, 2]

print(x is y)      # True (mesmo objeto na memória)
print(x is z)      # False (mesmo conteúdo, mas objetos diferentes)
print(x == z)      # True (mesmo conteúdo)

# Operador de associação:
print('c' in 'chat')      # True
print(3 in [1, 2, 3, 4])  # True
print(5 not in [1, 2])    # True

# O valor especial None:
# None representa ausência de valor ou nada.
# É do tipo NoneType, não é False, mas é tratado como falso em contextos booleanos.
# Você usa muito None para:
#    Variáveis sem valor definido
#    Retornos de funções que não retornam nada
#    Verificar se um valor foi atribuído ou não
a = None
print(type(a))        # <class 'NoneType'>
print(bool(a))        # False

# Conectivos Lógicos (Operadores lógicos):

# and – E lógico: Retorna True se ambos forem verdadeiros:
print(True and True)     # True
print(True and False)    # False

# Curiosidade: Python retorna o último valor avaliado, não só True/False.
print(5 and 3)   # 3
print(0 and 3)   # 0

# or – OU lógico: Retorna True se ao menos um for verdadeiro:
print(False or True)    # True
print(False or False)   # False

# Também retorna o primeiro valor verdadeiro:
print(0 or 3)     # 3
print(4 or 5)     # 4

# not – Negação: Inverte o valor
print(not True)      # False
print(not False)     # True
print(not 0)         # True
print(not 1)         # False

# Usando and e or em lógica: Veja mais sobre o if em condicionais.py
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")


# Verdadeiros e Falsos implícitos:
# Em contextos booleanos, Python trata alguns valores como False, mesmo sem serem do tipo bool.
# Considerados False:
#   . None
#   . False
#   . 0, 0.0, 0j
#   . '' (string vazia)
#   . [], {}, set(), () (coleções vazias)
# Considerados True:
#    Qualquer valor diferente dos acima, inclusive:
#        . Strings não vazias
#        . Números diferentes de 0
#        . Objetos/coleções com elementos
print(bool(0))      # False
print(bool(""))     # False
print(bool(1))      # True
print(bool("0"))    # True

# Boas práticas e curiosidades:
# Evite comparar diretamente com True/False:
# if ativo == True:     # Evite isso
# if ativo:             # Melhor assim

# Use is para comparar com None:
# if x is None:         # Correto

# bool() transforma qualquer valor em True ou False:
bool(0)       # False
bool('oi')    # True

# Expressões encadeadas:
if 18 <= idade < 60:
    print("Adulto")

# Curto-Circuito (Short-Circuit) em Python
# O curto-circuito é uma otimização lógica: Python evita avaliar expressões
# desnecessárias em operações com and e or.

# and: Se o primeiro operando for falso, não precisa avaliar o segundo — o
# resultado já será False.
print(False and print("Não aparece"))   # Nada é impresso

# or: Se o primeiro operando for verdadeiro, não precisa avaliar o segundo —
# o resultado já será True.
print(True or print("Também não aparece"))  # Nada é impresso

# Ex:
verifica = True
cond = False and verifica()  # "Função chamada" NÃO aparece
print(cond)

# Precedência Lógica: A precedência determina qual operador é avaliado primeiro
# quando tem mais de um na expressão.
#   Ordem:
#       1 - not (mais forte)
#       2 - and
#       3 - or (mais fraco)
resultado = True or False and False  # True or (False and False)  # => True or False => True
print(resultado)  # True

not_ = not True or False
# => (not True) or False
# => False or False => False
print(not_)     # False

# Dica: Use parênteses!
# Mesmo sabendo a precedência, usar parênteses melhora a legibilidade e evita erros:
valor = (((not True) and False) or not (True or False)) and False
print(valor)

# Operadores Bitwise (bit a bit):
# Esses operam bit a bit nos números inteiros. São muito usados em programação
# de baixo nível, redes, criptografia, compressão, etc.
# Antes, lembre que:
#   Decimal 5 = binário 0b0101
#   Decimal 3 = binário 0b0011
# Tabela dos operadores:
# Operador	        Nome	        Exemplo	    Resultado Binário	Decimal
#   &	      AND bit a bit	         5 & 3	    0101 & 0011 = 0001	  1
#   |	      OR bit a bit	         5 | 3	    0101 | 0011 = 0111    7
#   ^	      XOR bit a bit	         5 ^ 3	    0101 ^ 0011 = 0110	  6
#   ~	      NOT bit a bit	          ~5	    ~0101 = ...1010	     -6
#   <<	    Shift para a esquerda	 5 << 1	    0101 << 1 = 1010	  10
#   >>	    Shift para a direita	 5 >> 1	    0101 >> 1 = 0010	  2

# Detalhes e curiosidades:
# ~ (not bitwise): Inverte todos os bits de um número (inclusive o sinal).
# Em termos de matemática: ~x == -x - 1#
print(~5)   # -6
print(~0)   # -1

# Shift:
x = 2
n = 2
print(x << n)   # → desloca x n bits à esquerda (multiplica por 2ⁿ)
print(x >> n)   # → desloca x n bits à direita (divide por 2ⁿ, descartando fração)

# Exemplos práticos com bitwise:
# Verifica se um número é par (bit menos significativo = 0)
n = 6
if n & 1 == 0:
    print("Par")

# Liga/desliga bits como flags
PERMISSAO_ESCREVER = 0b010
PERMISSAO_LER = 0b100

permissoes = 0
permissoes |= PERMISSAO_LER   # liga a permissão de leitura
permissoes &= ~PERMISSAO_LER  # desliga a permissão de leitura

print(permissoes)

# Podemos fazer comparções com strings
# Ele lê por ordem alfabética, mas por trás dos panos ele lê
# segundo seus enderços na tabela ASCII:
print(f"a {ord('a')} > A {ord('A')}? {'a' > 'A'}")  # True

nome1 = "Fausto"
nome2 = "Maria"
print(nome1 == nome2)  # False

# Tecnicamente aqui ele percorre letra e por letra e verifica sua maioridade
print(nome1 <= nome2)  # True

# Uma representação simples, não é a mais eficiente, mas é para se ter uma análise
# Veja mais sobre o for em estrutura_repeticao_for.py
for i in range(len(nome1)):  # Pego do maior para realizar a leitura
    print(f"Letras: nome1({nome1})={nome1[i]} | nome2({nome2})={nome2[i]}")
    if ord(nome1[i]) <= ord(nome2[i]):
        print(
            f"SIM: {nome1[i]}({ord(nome1[i])})",
            f"é menor ou igual a {nome2[i]}({ord(nome2[i])})"
        )
        break
