import seaborn as sns

# Gráficos de calor
# Os gráficos de calor do Seaborn são excelentes para visualizar
# matrizes de dados, facilitando a identificação de padrões, correlações
# e concentrações de valores por meio de uma representação colorida das
# intensidades dos dados.

import matplotlib.pyplot as plt

# Carregar o conjunto de dados Iris
iris = sns.load_dataset('iris')
numerical_data = iris.select_dtypes(include=['float64'])

# Calcular a matriz de correlação
corr = numerical_data.corr()

# Criar o gráfico de calor
plt.figure(figsize=(10, 8))
sns.heatmap(corr, fmt='.2f', vmin=-1, vmax=1)

# Adicionar título
plt.title('Mapa de Calor da Correlação das Variáveis')

# Mostrar o gráfico
plt.show()
