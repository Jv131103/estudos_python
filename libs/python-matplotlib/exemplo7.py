import matplotlib.pyplot as plt

# Gráficos de caixas boxplot
# Os gráficos de caixa, mais conhecidos como boxplots,
# são ferramentas eficazes para visualizar a distribuição,
# a mediana e a variabilidade dos dados, destacando outliers
# e proporcionando uma visão clara da dispersão e assimetria
# dos conjuntos.

import numpy as np

# Definindo a área de plotagem
plt.figure(figsize=(12, 4))

# Dados de exemplo
np.random.seed(10)
dados = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Criar o boxplot
plt.boxplot(dados, tick_labels=['A', 'B', 'C'])

# Adicionar título e rótulos aos eixos
plt.title('Exemplo de Boxplot')
plt.xlabel('Grupos')
plt.ylabel('Valores')

# Mostrar o gráfico
plt.show()
