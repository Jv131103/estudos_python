import pandas as pd

# DataFrame pode ser comparado a uma tabela de banco de dados, com
# linhas e colunas rotuladas. É uma estrutura de dados bidimensional,
# Semelhante a estrutura de uma tabela em um banco relacional ou uma
# planilha do Excel. Cada uma das colunas é composta por uma Series
# alinhada por um índice comum

dados = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [100, 200, 300],
    'Quantidade': [10, 20, 30]
}

# Criando um DataFrame a partir de um dicionário
df = pd.DataFrame(dados)
print(df)
print()

# Acesso à coluna Produto
coluna = df['Produto']
print(f"Acesso a coluna Produto:\n{coluna}")
print()

# Acesso à múltiplas colunas
colunas = df[['Produto', 'Preço']]
print(f"Acesso as colunas Produtos e Preços:\n{colunas}")
print()

# Acesso à primeira linha pelo rótulo
linha = df.loc[0]
print(f"Acessando a primeira linha por rótulo:\n{linha}")
print()

# Acesso à primeira linha pela posição
linha = df.iloc[0]
print(f"Acessando a primeira linha pela posição:\n{linha}")
print()

# Acesso a um intervalo de linhas pela posição
interval = df.iloc[0:2]
print(f"intervalo entre as linhas 0 e 2:\n{interval}")
print()

# Acesso a um único valor pela coluna e linha
a = df['Produto'][0]
print(f"Acesso a um único valor pela coluna e linha: {a}")  # Saída: 'A'

# Acesso a um único valor pela linha e coluna
b = df.iloc[0]['Produto']
print(f"Acesso a um único valor pela linha e coluna: {b}")  # Saída: 'A'
