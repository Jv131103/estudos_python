nome = "UserPython"

# Acessando por índices
print(nome[0])  # Indices começam sempre por 0 e vai até tamanho -1

# Fatiamento / slicing
# string[inicio:fim:intervalo]
# Pegar de trás para frente: string[::-1]
print(nome[:2])

# Tamanho da string
print(len(nome))  # O tamanho começa sempre contando do primeiro elemento até o último

# Verificação
# Pense assim: x in algo (x está/pertence/entra/contém em algo)
# Pense assim: x not in algo (x não está/pertence/entra/contém em algo)
print(nome in "UserPython UserPython")  # Este exemplo é uma verificação
print(nome not in "UserPython UserPython")  # Este exemplo é uma negação da verificação

# Outros
nome = "João"

# Converter strings para minúsculas
# Podemos definir em entradas de dados: nome = input("Nome: ").lower()
print(nome.lower())

# Converter strings para maiúsculas
# Podemos definir em entradas de dados: nome = input("Nome: ").lower()
print(nome.upper())

# Converter para título
print(nome.title())

# Converter apenas a primeira letra em Maiúscula
print("teste".capitalize())

# Remover espaços
ling = "     Python     "
print(ling.rstrip(), "outro")  # Remove espaços a direita
print(ling.lstrip(), "outro")  # Remove espaços a esquerda
print(ling.strip(), "outro")   # Remove espaços a esquerda e a direita

# Você pode usar mais de uma função especial
print(ling.upper().strip())

# Realizando busca da posição de um valor da string
nome = "João Davi"
print(nome.lower().index('j'))

# Quebrando uma string de forma específica
nome = "João Davi ; Anathália"
print(nome.split())  # Remove o que têm espaços
print(nome.split(";"))  # Remove por um caractere específico
