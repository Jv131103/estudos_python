import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

dados_usuarios = {
    "horas_tela": [1, 8, 2, 9, 5, 7, 1.5, 6, 4, 8.5],
    "qtd_apps": [3, 15, 4, 18, 8, 12, 2, 14, 7, 16]
}

df = pd.DataFrame(dados_usuarios)
print(df)

print("Tratando Valores nulos...")
df["horas_tela"] = df["horas_tela"].fillna(df["horas_tela"].mean())
df["qtd_apps"] = df["qtd_apps"].fillna(df["qtd_apps"].mean())

# Como não existe 'y', TODAS as colunas são usadas como X
X = df[["horas_tela", "qtd_apps"]]

# Padronizar as escalas (FUNDAMENTAL para o KMeans)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Criar e treinar o modelo KMeans (exemplo: criando 2 grupos/clusters)
kmeans = KMeans(n_clusters=3, random_state=42)

# Observe que passamos apenas X no método fit/predict!
df['cluster'] = kmeans.fit_predict(X_scaled)

# Exibe a tabela com o número do grupo (cluster) atribuído a cada registro
print(df)
print()
print(df.groupby("cluster")[["horas_tela", "qtd_apps"]].mean())
