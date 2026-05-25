from sklearn.datasets import fetch_openml

# Carrega o dataset fornecido pelo site do openml
data = fetch_openml('Worldwide-Meat-Consumption', as_frame=True)

# Exibindo a descrição do dataset
print(data.DESCR)

# Exibindo os nomes das características
print(data.feature_names)

# Exibindo as primeiras linhas do DataFrame
data.frame.head()
