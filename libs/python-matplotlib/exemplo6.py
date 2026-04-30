import matplotlib.pyplot as plt

# Gráfico de pizza
# Os gráficos de pizza são ideais para visualizar a proporção
# de diferentes categorias em um conjunto de dados, facilitando
# a compreensão das partes que compõem o todo. No entanto, esse
# tipo de gráfico pode ser difícil de interpretar quando há
# muitas divisões ou quando as diferenças entre os valores são 
# pequenas, ou seja, nessas situações podem ocasionar uma 
# visualização confusa e menos precisa das informações 
# comparadas.

# Definindo a área de plotagem
plt.figure(figsize=(4, 4))

# Dados de exemplo
ids = ['A', 'B', 'C', 'D']
valores = [15, 30, 45, 10]
cores = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Criar o gráfico de pizza
plt.pie(valores, labels=ids, colors=cores, autopct='%1.1f%%')

# Adicionar título
plt.title('Gráfico de Pizza')

# Mostrar o gráfico
plt.show()
