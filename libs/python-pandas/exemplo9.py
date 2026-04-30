import pandas as pd

# Leitura e escrita de arquivos
dados = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [100, 200, 300],
    'Quantidade': [10, 20, 30]
}

# Criando um DataFrame a partir de um dicionário
df = pd.DataFrame(dados)

# Escrevendo um DataFrame para um arquivo CSV
df.to_csv('./libs/python-pandas/dados.csv', sep=';', index=False)

# Lendo o arquivo CSV criado, para um novo DataFrame
df2 = pd.read_csv('./libs/python-pandas/dados.csv', sep=';')
print(df2)
