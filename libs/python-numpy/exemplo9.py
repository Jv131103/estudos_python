import numpy as np

# Processamento de estatística descritivo por eixo e total
# Simulação de dados de vendas com dados aleatórios
# Os resultados deverão mudar a cada execução
vendas = np.random.randint(100, 200, size=(30, 4))

# axis=0 → desce nas linhas, resultado por coluna
# axis=1 → anda nas colunas, resultado por linha

# Média de vendas por semana
media_semanal = np.mean(vendas, axis=0)

# Menores vendas por semana
menor_semanal = np.min(vendas, axis=0)

# Total de vendas por mês
total_mensal = np.sum(vendas)

# Maior venda do mês
maior_mensal = np.max(vendas)

print(media_semanal)  # Saída: [149.76 154.03 161.26 148.8]
print(menor_semanal)  # Saída: [101 100 112 105]
print(total_mensal)  # Saída: 18416
print(maior_mensal)  # Saída: 199
