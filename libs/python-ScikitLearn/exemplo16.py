# Imports
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import DBSCAN, KMeans

df = pd.read_csv("./libs/python-ScikitLearn/moons.csv")
print(df.head())

# Plotando os dados
plt.scatter(x=df["X"], y=df["Y"])
plt.show()

# Definição dos algoritmos
km = KMeans(n_clusters=4, random_state=42)
db = DBSCAN(eps=0.4)

# Aplicar os algoritmos sobre os pontos, obtendo os clusteres resultantes
c_km = km.fit_predict(df)
c_db = db.fit_predict(df)

df["label_kmeans"] = c_km
df["label_dbscan"] = c_db

# Plotando as diferenças
fig = plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title("Original")
plt.scatter(x=df["X"], y=df["Y"])

plt.subplot(2, 2, 3)
plt.title("K-means")
plt.scatter(x=df["X"], y=df["Y"], c=df["label_kmeans"])

plt.subplot(2, 2, 4)
plt.title("DBSCAN")
plt.scatter(x=df["X"], y=df["Y"], c=df["label_dbscan"])

plt.show()

dados = pd.read_csv("./libs/python-ScikitLearn/mall.csv")
print(dados.head())
print(dados.info())

sns.pairplot(dados)
plt.show()

# Instancia o algoritmo
kmeans = KMeans(n_clusters=5, random_state=42)

# Implementa o k-means sobre os dados
kmeans.fit(dados[["Annual Income (k$)", "Spending Score (1-100)"]])

# Obtém os centroids do método
centroids = kmeans.cluster_centers_

# Salva os labels (grupos) dos clusteres para cada exemplo
kmeans_labels = kmeans.predict(
    dados[
        [
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ]
)

# Plotando a clusterização
plt.scatter(dados["Annual Income (k$)"],      # Eixo X
            dados["Spending Score (1-100)"],  # Eixo Y
            c=kmeans_labels,                  # Esquema de cores (quantas usar)
            alpha=0.5,                        # Transparência dos pontos
            cmap="rainbow")                   # Paleta de cores
plt.xlabel("Salário anual")
plt.ylabel("Pontuação de gastos")

# Plotando os centrois
plt.scatter(centroids[:, 0],                 # Eixo X dos centroids
            centroids[:, 1],                 # Eixo Y dos centroids
            c="black",                       # Todos os centroids são pretos
            marker="X",                      # Marcação como um "X"
            s=200)                           # Tamanho da marcação

plt.show()

k = list(range(1, 10))

sse = []
for i in k:
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(dados[["Annual Income (k$)", "Spending Score (1-100)"]])
    sse.append(kmeans.inertia_)

plt.plot(k, sse, "-o")
plt.xlabel("Número de clusteres")
plt.ylabel("Inércia (Soma dos Erros Quadráticos)")
plt.show()

# Instancia o algoritmo
dbscan = DBSCAN(eps=10, min_samples=8)

# Roda o algoritmo sobre os dados
dbscan.fit(dados[["Annual Income (k$)", "Spending Score (1-100)"]])

# Obtém as atribuições dos pontos
dbscan_labels = dbscan.labels_

plt.scatter(dados["Annual Income (k$)"],      # Eixo X
            dados["Spending Score (1-100)"],  # Eixo Y
            c=dbscan_labels,                  # Esquema de cores
            alpha=0.5,                        # Transparência dos pontos
            cmap="rainbow")                   # Paleta de cores
plt.xlabel("Salário anual")
plt.ylabel("Pontuação de gastos")
plt.show()

# Removendo os outliers (cluster "-1")
mascara = dbscan_labels >= 0

plt.scatter(dados["Annual Income (k$)"][mascara],      # Eixo X
            dados["Spending Score (1-100)"][mascara],  # Eixo Y
            c=dbscan_labels[mascara],                  # Esquema de cores
            alpha=0.5,                                 # Transparência dos pontos
            cmap="rainbow")                            # Paleta de cores
plt.xlabel("Salário anual")
plt.ylabel("Pontuação de gastos")
plt.show()

dados['kmeans'] = kmeans_labels  # Salva os clusters do K-Means no DataFrame
dados['dbscan'] = dbscan_labels  # Salva os clusters do DBSCAN no DataFrame

print(dados[dados["kmeans"] == 2].describe())  # ganha pouco e gasta pouco
print(dados[dados["kmeans"] == 4].describe())  # ganha bem e gasta muito
