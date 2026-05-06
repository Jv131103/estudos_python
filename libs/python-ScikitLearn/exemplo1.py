from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder
import pandas as pd


df = pd.read_csv("./csvs/exemplos_limpeza_dados.csv")
print(df.shape)
print()

# Pegando uma amostra de 5 linhas aleatórias
df.sample(5)

# Explorando a base
df.info()

# Exibe estatísticas básicas do dataframe
df.describe()

# Remover dados duplicados em nova variável
df_unicos = df.drop_duplicates()

# Remover dados duplicados na MESMA variável
df.drop_duplicates(inplace=True)

# Apagar dados faltantes na MESMA variável
df_unicos.dropna(inplace=True)

# Preencher dados faltantes
# - coloca o valor médio da idade na coluna Age
df["Age"].fillna(df["Age"].mean(), inplace=True)

# - coloca o valor mediano do salário na coluna Salary
df["Salary"].fillna(df["Salary"].median(), inplace=True)

# Tratando dados categóricos - ORDINAIS
print(df["Purchased"].unique())  # valores únicos

le = LabelEncoder()

df["Purchased_encoder"] = le.fit_transform(df["Purchased"])
df["Grade_encoder"] = le.fit_transform(df["Grade"])

# print(df)

# Tratando dados categóricos - NOMINAIS
aux = pd.get_dummies(df["Country"])
final = pd.concat([df, aux], axis=1)
# print(final)

# Filtrar colunas relevantes
final.drop(columns=["Country", "Grade", "Purchased"], inplace=True)
# print(final)

# Transforma os dados com Padronização/Normalização
sc = StandardScaler()
final_padronizado = sc.fit_transform(final)

mm = MinMaxScaler(feature_range=(10, 20))
final_normalizado = mm.fit_transform(final)


# Salvar os dados padronizados em outro dataframe
df_final_padronizado = pd.DataFrame(
    final_padronizado,
    columns=final.columns
)
print(df_final_padronizado)

print()

# Salvar os dados normalizados em outro dataframe
df_final_normalizado = pd.DataFrame(
    final_normalizado,
    columns=final.columns
)
print(df_final_normalizado)

# Exporta os dados para arquivos
df_final_padronizado.to_csv("./csvs/dados_padronizados.csv")
df_final_normalizado.to_csv("./csvs/dados_normalizados.csv")
