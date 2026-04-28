import numpy as np

# Resolulção de sistemas lineares
# Resolver um sistema linear significa encontrar os valores
# das variáveis que satisfaçam todas as equações simultaneamente.
# Considere o sistemas de equações lineares 3x + 2y = 5
# e x + 2y = 5 na forma matricial Ax = B. A função
# np.linalg.solve resolve esse sistema linear encontrado
# os valores de x que satisfazem a equação.

# Coeficientes do sistema linear
a = np.array([[3, 2], [1, 2]])
b = np.array([5, 5])

# Resolvendo o sistema
solucao = np.linalg.solve(a, b)

print(solucao)  # Saída: [0. 2.5]
