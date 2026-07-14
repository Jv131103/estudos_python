# import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dados (idade, salário)
clientes = [
    [18, 1500],
    [20, 1800],
    [22, 2000],
    [25, 2500],
    [40, 7000],
    [42, 7500],
    [45, 8000],
    [47, 8500],
]

modelo = KMeans(
    n_clusters=2,
    random_state=42
)

modelo.fit(clientes)

# Grupo 0: (18, 20, 22, 25 anos)
# Grupo 1: (40, 42, 45, 47 anos)
print(modelo.labels_)
