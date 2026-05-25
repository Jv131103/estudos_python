import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

# Criando o conjunto de dados fictício
data = {
    'Cultura': ['Milho', 'Soja', 'Café', 'Cana-de-açúcar', 'Arroz', 'Algodão'],
    'Região': ['Norte', 'Sul', 'Sudeste', 'Nordeste', 'Centro-Oeste', 'Nordeste'],
    'Produção (toneladas)': [5000, 12000, 8000, 15000, 11000, 7000],
    'Preço por Tonelada (R$)': [750, 1300, 2000, 600, 900, 1400],
    'Tipo de Solo': ['Argiloso', 'Arenoso', 'Misto', 'Argiloso', 'Arenoso', 'Misto']
}

# Convertendo em DataFrame
df = pd.DataFrame(data)
df.head()

# Inicializando o LabelEncoder
label_encoder = LabelEncoder()

# Aplicando Label Encoding na coluna 'Cultura'
df['Cultura_LabelEncoded'] = label_encoder.fit_transform(df['Cultura'])

print(df[['Cultura', 'Cultura_LabelEncoded']])
print()

# Inicializando o OneHotEncoder
onehot_encoder = OneHotEncoder(sparse_output=False)

# Aplicando One-Hot Encoding na coluna 'Região'
onehot_encoded = onehot_encoder.fit_transform(df[['Região']])

# Convertendo para DataFrame para fácil visualização
encoded_columns = onehot_encoder.get_feature_names_out(['Região'])
onehot_df = pd.DataFrame(onehot_encoded, columns=encoded_columns)

# Juntando os resultados ao DataFrame original
df = pd.concat([df, onehot_df], axis=1)
df[['Região', 'Região_Centro-Oeste', 'Região_Nordeste', 'Região_Norte', 'Região_Sul', 'Região_Sudeste']]

print(df)
print()

# Aplicando Ordinal Encoding na coluna 'Tipo de Solo'
ordinal_encoder = OrdinalEncoder(categories=[['Arenoso', 'Argiloso', 'Misto']])
df['TipoSolo_OrdinalEncoded'] = ordinal_encoder.fit_transform(df[['Tipo de Solo']])

df[['Tipo de Solo', 'TipoSolo_OrdinalEncoded']]

print(df)
print()
