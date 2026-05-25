import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
import seaborn as sns


# Carregar o dataset California Housing
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = pd.Series(housing.target, name='MedHouseVal')

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Testando diferentes algoritmos de regressão

# Regressão Linear
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
r2 = model_lr.score(X_test, y_test)
print(f"Performance do modelo: {r2:.2f}")

# Regressão Ridge
model_ridge = Ridge(alpha=1.0)
model_ridge.fit(X_train, y_train)
r2 = model_ridge.score(X_test, y_test)
print(f"Performance do modelo: {r2:.2f}")

# Regressão com Random Forest
model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)
r2 = model_rf.score(X_test, y_test)
print(f"Performance do modelo: {r2:.2f}")


centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=750, centers=centers, cluster_std=0.4, random_state=0
)

X_scaled = StandardScaler().fit_transform(X)

# Exibe os dados
plt.scatter(X[:, 0], X[:, 1])
plt.show()


# Aplicando K-Means com 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# Aplicando DBSCAN
dbscan = DBSCAN(eps=0.3, min_samples=10)
dbscan_labels = dbscan.fit_predict(X_scaled)

# Visualizando os clusters criados pelo K-Means
plt.figure(figsize=(12, 6))

# Gráfico para K-Means
plt.subplot(1, 2, 1)
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=kmeans_labels, palette='viridis', s=50)
plt.title('Clusters criados pelo K-Means')

# Gráfico para DBSCAN
plt.subplot(1, 2, 2)
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=dbscan_labels, palette='viridis', s=50)
plt.title('Clusters criados pelo DBSCAN')

plt.show()
