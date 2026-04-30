import pandas as pd

# Junção (Join)
# A junção é utilizada para combinar DataFrames com base
# em uma chave comum, semelhante a joins em bancos de
# dados relacionais. Isso pode ser feito de várias maneiras,
# como junção interna, externa, à esquerda ou à direita,
# determinando como os dados são alinhados e quais linhas são
# mantidas ou descartadas.

# DataFrame de produtos com 'ProdutoID' como índice
df_produtos = pd.DataFrame({
    'ProdutoID': [1, 2, 3, 4],
    'NomeProduto': ['Prod A', 'Prod B', 'Prod C', 'Prod D']
}).set_index('ProdutoID')

# DataFrame de vendas com 'ProdutoID' como índice
df_vendas = pd.DataFrame({
    'VendaID': [101, 102, 103, 104],
    'ProdutoID': [1, 2, 2, 4],
    'Quantidade': [10, 5, 15, 7]
}).set_index('ProdutoID')

# Realizar o join com base no índice 'ProdutoID'
df_combinado = df_vendas.join(df_produtos, how='inner')
print(f"Join combinado:\n{df_combinado}")
