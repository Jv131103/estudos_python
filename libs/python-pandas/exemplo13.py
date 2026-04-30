import pandas as pd
import matplotlib.pyplot as plt


# Integração nativa com visualização de dados
# Dados de exemplo de vendas mensais
data = {
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'Vendas': [2500, 2700, 3000, 3200, 3100, 3300]
}

# Criar DataFrame e plotar um gráfico de linha
df = pd.DataFrame(data)
df.plot(x='Mês', y='Vendas', marker='o', color='b')

plt.show()
