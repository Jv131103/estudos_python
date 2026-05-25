from sklearn.datasets import load_iris

# Carrega o dataset
iris = load_iris()

# Acessar dados e rótulos
X, y, name = iris.data, iris.target, iris.feature_names

print("Características:\n", X[:5])
print("Rótulos:\n", y[:5])
print("Nome das características:\n", name)

# Acessar metadados
print("Metadados:\n", iris.DESCR)
