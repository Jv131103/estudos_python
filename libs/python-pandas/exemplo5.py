import pandas as pd

dados = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [100, 200, 300],
    'Quantidade': [10, 20, 30]
}
df = pd.DataFrame(dados)

# Ordenação dos dados:
# Ordenação de dados em ordem crescente
df_ordenado = df.sort_values(by='Preço')
print(f"Preço ordenado:\n{df_ordenado}")
print()

# Ordenação de dados em ordem decrescente
df_ordenado_desc = df.sort_values(by='Preço', ascending=False)
print(f"Preço ordenado em decrescente:\n{df_ordenado_desc}")
print()

# Ordenação de dados por múltiplas colunas
df_ordenado_mult = df.sort_values(by=['Preço', 'Quantidade'])
print(f"Preço e Qualtidade ordenados:\n{df_ordenado_mult}")
print()
