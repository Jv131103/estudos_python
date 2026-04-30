import pandas as pd

# filtragem de dados
dados = {
    'Produto': ['A', 'B', 'C'],
    'Preço': [100, 200, 300],
    'Quantidade': [10, 20, 30]
}
df = pd.DataFrame(dados)

# Filtragem de dados com base em uma condição
produtos_caros = df[df['Preço'] > 150]

# Filtragem com múltiplas condições
produtos_caros_quantidade_alta = df[
    (df['Preço'] > 150) & (df['Quantidade'] > 20)
]

