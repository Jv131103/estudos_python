import seaborn as sns

# Gráficos de categorização
# Os gráficos de categorização do Seaborn, como boxplots e violin plots,
# são eficazes para visualizar a distribuição e a variabilidade dos dados
# em diferentes categorias, destacando padrões entre grupos de maneira
# clara e objetiva.

import matplotlib.pyplot as plt

# Dados de exemplo
tips = sns.load_dataset('tips')

# Definindo a área de plotagem
plt.figure(figsize=(12, 6))

# Criar o boxplot
plt.subplot(1, 2, 1)
sns.boxplot(data=tips, x='day', y='total_bill')

plt.title('Boxplot do Total da Conta por Dia')
plt.xlabel('Dia da Semana')
plt.ylabel('Total da Conta')

# Criar o violin plot
plt.subplot(1, 2, 2)
sns.violinplot(data=tips, x='day', y='total_bill')

plt.title('Violin Plot do Total da Conta por Dia')
plt.xlabel('Dia da Semana')
plt.ylabel('Total da Conta')

# Ajustar layout e mostrar o gráfico
plt.tight_layout()
plt.show()
