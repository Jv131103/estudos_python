import pandas as pd

# Mesclagem (Merge)
# A mesclagem oferece um controle mais granular e flexível sobre
# a combinação de DataFrames, permitindo especificar múltiplas
# chaves e tipos de junções

# DataFrame de produtos
df_produtos = pd.DataFrame({
    'ProdutoID': [1, 2, 3, 4],
    'NomeProduto': ['Prod A', 'Prod B', 'Prod C', 'Prod D']
})

# DataFrame de vendas
df_vendas = pd.DataFrame({
    'VendaID': [101, 102, 103, 104],
    'ProdutoID': [1, 2, 2, 4],
    'Quantidade': [10, 5, 15, 7]
})

# Realizar o merge com base na coluna 'ProdutoID'
df_combinado = pd.merge(df_vendas, df_produtos, on='ProdutoID', how='inner')
print(f"Combinando os dataframes:\n{df_combinado}")
