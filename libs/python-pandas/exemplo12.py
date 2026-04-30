import pandas as pd

# Análise de séries temporais
# A análise de séries temporais é uma área da Estatística e da Ciência
# de Dados que se concentra em estudar dados coletados ou observados
# sequencialmente ao longo do tempo. O Pandas fornece ferramentas úteis
# para manipulação e análise de dados temporais, facilitando tarefas como
# resampling, cálculo de médias móveis, análise de sazonalidade e
# tendências presentes nas amostras. Séries temporais são especialmente
# importantes em campos como finanças, economia, meteorologia e muitas
# outras áreas no qual o tempo é uma variável crucial. Além disso, esse
# método de análise geralmente antecede a implementação de modelos
# mais robustos baseados em algoritmos de Machine Learning (Kaggle, 2024).
import numpy as np

# Criando uma série temporal de exemplo
datas = pd.date_range(start='2026-01-01', periods=100, freq='D')

# Série temporal acumulada com ruído
dados = np.random.randn(100).cumsum()
ts = pd.Series(dados, index=datas)

# Calculando a média móvel de 3 dias
rolling_mean_3 = ts.rolling(window=3).mean()

# Exibindo os top 10 resultados da média móvel de 3 dias
print(rolling_mean_3.head(10))
