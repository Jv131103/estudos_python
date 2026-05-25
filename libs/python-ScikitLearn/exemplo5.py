from sklearn.datasets import make_classification
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

X, y = make_classification(n_samples=300,        # Número de amostras
                           n_features=3,         # Número total de características
                           n_informative=3,      # Número de características informativas
                           n_redundant=0,        # Número de características redundantes
                           n_clusters_per_class=1,  # Número de clusters por classe
                           n_classes=3,          # Número de classes
                           random_state=0)      # Semente para reprodução dos resultados

# Criando um DataFrame para visualização
df = pd.DataFrame(X, columns=['Feature 1', 'Feature 2', 'Feature 3'])
df['Target'] = y

print(df.head())  # Mostrando as primeiras linhas do DataFrame

# Visualização 2D das duas primeiras características
plt.figure(figsize=(8, 6))
plt.scatter(df['Feature 1'], df['Feature 2'], c=df['Target'], cmap='viridis', edgecolor='k', s=50)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('2D Scatter Plot of Classification Data with 3 Classes')
plt.colorbar(label='Target Class')
plt.grid(True)
plt.show()

# Criando o gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Usando uma paleta de cores
colors = plt.cm.viridis(df['Target'] / np.max(df['Target']))

# Adicionando o scatter plot 3D
scatter = ax.scatter(df['Feature 1'], df['Feature 2'], df['Feature 3'], c=colors, s=100, edgecolor='k', alpha=0.7)

# Adicionando rótulos aos eixos
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')

# Definindo o título
ax.set_title('3D Plot')

# Exibindo o gráfico
plt.show()
