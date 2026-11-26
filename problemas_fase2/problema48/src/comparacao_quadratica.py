from mse import calcular_mse_quadratico
from treinar_modelo_quadratico import treinar_modelo_quadratico

dados = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50)
]

a, peso, bias, historico = treinar_modelo_quadratico(
    dados,
    a_inicial=0.001,
    peso_inicial=0.2,
    bias_inicial=30,
    learning_rate=0.00000001,
    epocas=10
)
mse_treino = calcular_mse_quadratico(dados, a, peso, bias)
print(f"MSE Quadrático: {mse_treino}")

dados_teste = [
    (10, 33),
    (40, 37),
    (80, 47)
]
mse_teste = calcular_mse_quadratico(dados_teste, a, peso, bias)
print(f"MSE teste: {mse_teste}")
