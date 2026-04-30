import pandas as pd

# Agregação dos dados:
# Agregar dados, refere-se à aplicação de funções de rusumo aos dados,
# como soma, média, contagem, etc. É responsável para se chegar a ter
# uma visão dos dados e identificar padrões ou tendências
dados = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [100, 200, 300],
    'Quantidade': [10, 20, 30]
}
df = pd.DataFrame(dados)


# Agregação de dados - soma total
total_vendas = df['Preço'].sum()
print(total_vendas)  # Saída: 600
print()

# Agregação de dados - média
media_precos = df['Preço'].mean()
print(media_precos)  # Saída: 200
print()

# Agregação de dados por grupo – gera uma tabela sumarizada
vendas_por_produto = df.groupby('Produto').sum()
print(vendas_por_produto)
