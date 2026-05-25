from sklearn.datasets import load_wine
import pandas as pd
import numpy as np

# Carregando o dataset
wine = load_wine()
X = wine.data  # Características
y = wine.target  # Rótulos

# Convertendo para DataFrame para melhor visualização
df = pd.DataFrame(X, columns=wine.feature_names)
df['target'] = y
df.head()

print(df)
