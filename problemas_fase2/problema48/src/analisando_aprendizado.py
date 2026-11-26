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

print("++" * 20)
for idx, epoca in enumerate(historico, start=1):
    print(f"{idx}° mse: {epoca}")
    print("--" * 20)

assert len(historico) == 11

assert historico[-1] < historico[0]

assert abs(historico[0] - 27.65625) < 1e-10
