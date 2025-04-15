# Uma string é uma sequência imutável de caracteres. Isso quer dizer que:
#  - Cada caractere pode ser acessado por índice.
#  - Strings não podem ser alteradas diretamente (imutabilidade).
#  - Strings são objetos do tipo str.

nome = "João"
print(type(nome))  # <class 'str'>

# Aspas simples
s1 = 'Olá'

# Aspas duplas
s2 = "Mundo"

# Aspas triplas (usadas para texto multilinha ou docstrings)
s3 = '''Texto
com várias
linhas'''

# Índices e Fatiamento
# Strings são indexadas como listas:
texto = "Python"

# Índices
print(texto[0])   # 'P'
print(texto[-1])  # 'n' (último)

# Fatiamento
print(texto[0:2])   # 'Py' (início incluso, fim exclusivo)
print(texto[:3])    # 'Pyt'
print(texto[2:])    # 'thon'
print(texto[::2])   # 'Pto' (de 2 em 2)
print(texto[::-1])  # 'nohtyP' (reverso)

# Imutabilidade
# Atenção: Strings, são objetos imutáveis, ous seja, não podemos alterar os seus valores
nome = "João"
# nome[0] = "M"  # Erro! Strings não podem ser alteradas diretamente
# Correto:
novo_nome = "M" + nome[1:]
print(novo_nome)

# Operações com strings:
a = "Olá"
b = "Mundo"
print(a + " " + b)      # Concatenação
print(a * 3)            # Repetição
print(len(a))           # Tamanho
print("a" in a)         # Verificação de caractere

# Funções e Métodos

# Capitalização e formatos
s = "python é legal"

print(s.capitalize())   # Python é legal (só a 1ª letra maiúscula)
print(s.title())        # Python É Legal
print(s.upper())        # PYTHON É LEGAL
print(s.lower())        # python é legal
print(s.swapcase())     # PYTHON É LEGAL → python É LEGAL

# Remoção e preenchimento
s = "  Olá  "

print(s.strip())      # Remove espaços das pontas
print(s.lstrip())     # Remove só da esquerda
print(s.rstrip())     # Remove só da direita

print("42".zfill(5))   # Preenche com zeros à esquerda → '00042'
print("hi".center(10, "-"))  # '--hi------'

# Pesquisa e substituição
s = "banana"

print(s.find("na"))        # 2 (posição da 1ª ocorrência)
print(s.rfind("na"))       # 4 (última ocorrência)
print(s.index("na"))       # 2 (igual ao find, mas lança erro se não achar)
# print(s.index("x"))      # ValueError

print(s.replace("na", "xo"))  # baxoxo

# Divisão e junção
s = "um,dois,três"

print(s.split(","))     # ['um', 'dois', 'três']
print(" - ".join(['A', 'B', 'C']))  # 'A - B - C'

# Verificação com is:
# Veja completo no arquivo tipos_de_dados_e_conversoes.py
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("abc".islower())     # True
print("ABC".isupper())     # True
print("Python".istitle())  # True
print(" ".isspace())       # True

# Outros úteis:
print("python".startswith("py"))  # True
print("python".endswith("on"))    # True
print("linha\noutra".splitlines())  # ['linha', 'outra']

# split, para dividir e quebrar a string
nome = "Joao"
nome = nome.split("o")
print(nome)  # ['J', 'a', '']

# Defininido entrada com split
nome, sobrenome = input("Digite seu nome e depois sobrenome: ").split(" ")  # Pode definir como quiser aqui
print(nome, sobrenome)

# Caracteres especiais:
# Código	Significado
# \n	    Nova linha
# \t	    Tabulação
# \\	    Barra invertida
# \'	    Aspas simples
# \"	    Aspas duplas
print("\"Olá\nMundo\"")  # quebra de linha

# Métodos Menos Usados mas Úteis
s = "João:Gonçalves"
print(s.partition(":"))  # Saída: ('João', ':', 'Gonçalves') - começa da esquerda.

s = "arquivo.backup.zip"
print(s.rpartition("."))  # Saída: ('arquivo.backup', '.', 'zip') - começa da direita.

texto = "Nome\tIdade"
print(texto.expandtabs(4))  # Saída: 'Nome    Idade'  (Bom substituto do \t)

# Como lower(), mas mais agressivo, ideal para comparações sem case (especialmente com idiomas).
print("Straße".casefold())  # Alemão para "rua"
print("straße".casefold())  # Ambas saem como 'strasse'

nome = "sr_joao"
print(nome.removeprefix("sr_"))  # joao

arquivo = "relatorio.pdf"
print(arquivo.removesuffix(".pdf"))  # relatorio

print("42".zfill(5))  # Saída: '00042'  ()qtd de zeros a esquerda contando coms os valores já tido

print("Oi".center(10, "-"))  # ----Oi----
