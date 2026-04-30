import pandas as pd


# Concatenação
# A concatenação é utilizada para empilhar no sentido vertical ou
# horizontal, geralmente para adicionar novas linhas ou colunas em um
# Dataframe existente.

# DataFrame de vendas no primeiro semestre
df_vendas1 = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Vendas': [2000, 2200, 2500, 2700, 2600, 2900]
})

# DataFrame de vendas no segundo semestre
df_vendas2 = pd.DataFrame({
    'Mês': ['Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Vendas': [3100, 3300, 3200, 3400, 3500, 3600]
})

# Concatenar DataFrames verticalmente
df_vendas_completo = pd.concat([df_vendas1, df_vendas2], ignore_index=True)
print(f"DataFrame concatenado: {df_vendas_completo}")
