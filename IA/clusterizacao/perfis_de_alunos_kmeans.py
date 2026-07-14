from sklearn.cluster import KMeans

alunos = [
    [9, 95],
    [8, 90],
    [2, 30],
    [1, 20],
    [7, 88],
    [3, 35]
]

modelo = KMeans(
    n_clusters=2,
    random_state=42
)

modelo.fit(alunos)

# Cada aluno é representado por: [nota, frequência]
# O algoritmo provavelmente formará:
#   Grupo 1: (Notas altas, Boa frequência)
#   Grupo 0: (Notas baixas. Pouca frequência)
print(modelo.labels_)
