import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

dados_clientes = {
    "idade": [25, 45, 23, 52, 34, 46, 22, 50],
    "gasto_mensal": [200, 800, 150, 900, 400, 850, 180, 950]
}

df = pd.DataFrame(dados_clientes)
print(df)

# Tratamento
print("Tratando Valores nulos...")
df["idade"] = df["idade"].fillna(df["idade"].mean())
df["gasto_mensal"] = df["gasto_mensal"].fillna(0)

# Como não existe 'y', TODAS as 3 colunas são usadas como X
X = df[["idade", "gasto_mensal"]]

# Padronizar as escalas (FUNDAMENTAL para o KMeans)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Criar e treinar o modelo KMeans (exemplo: criando 2 grupos/clusters)
kmeans = KMeans(n_clusters=2)

# Observe que passamos apenas X no método fit/predict!
df['cluster'] = kmeans.fit_predict(X_scaled)

# Exibe a tabela com o número do grupo (cluster) atribuído a cada registro
print(df)
print()
print(df.groupby("cluster")[["idade", "gasto_mensal"]].mean())
