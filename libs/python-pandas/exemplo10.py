import pandas as pd

# Limpeza e preparação dos dados
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [23, 35, 45, None, 28],
    'Salário': [50000, 60000, None, 70000, 80000]
}

# Criação de DataFrame com valores nulos (None)
df = pd.DataFrame(data)

# Removendo linhas com valores ausentes
df_cleaned = df.dropna()

# Preenchendo valores ausentes com a média
df['Idade'] = df['Idade'].fillna(df['Idade'].mean())
df['Salário'] = df['Salário'].fillna(df['Salário'].mean())

print(df)
