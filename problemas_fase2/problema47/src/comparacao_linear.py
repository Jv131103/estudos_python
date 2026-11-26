from mse import calcular_mse
from treinar_modelo_completo import treinar_modelo_completo

dados = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50)
]

peso, bias, historico = treinar_modelo_completo(
    dados,
    peso_inicial=0.1,
    bias_inicial=30,
    learning_rate=0.0001,
    epocas=10
)

mse_treino = calcular_mse(dados, peso, bias)
print(f"MSE Linear: {mse_treino}")

dados_teste = [
    (10, 33),
    (40, 37),
    (80, 47)
]
mse_teste = calcular_mse(dados_teste, peso, bias)
print(f"MSE teste: {mse_teste}")
