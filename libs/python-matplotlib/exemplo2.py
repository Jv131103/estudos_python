import matplotlib.pyplot as plt

# Gráfico de Barra
# Gráficos de barra são ideais para comparar valores entre
# diferentes categorias, proporcionando uma visualização clara
# e intuitiva das diferenças entre os dados.

# Definindo a área de plotagem
plt.figure(figsize=(12, 6))

# Dados de exemplo
categorias = ['A', 'B', 'C', 'D', 'E', 'F']
valores = [10, 20, 15, 30, 25, 22]

# Gráfico de barras
plt.bar(categorias, valores, color='orange')

# Configurando as propriedades do gráfico
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.title('Gráfico de Barras')

# Exibindo o gráfico
plt.show()
