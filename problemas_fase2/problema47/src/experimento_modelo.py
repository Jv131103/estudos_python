try:
    from comparar_desempenho import comparar_desempenho
    from treinar_modelo_completo import treinar_modelo_completo
except (ImportError, ImportWarning):
    from src.comparar_desempenho import comparar_desempenho
    from src.treinar_modelo_completo import treinar_modelo_completo


dados_treino = [
    (0, 30),
    (25, 35),
    (50, 40),
    (75, 45),
    (100, 50)
]

dados_teste = [
    (10, 33),
    (40, 37),
    (80, 47)
]

# 1. Treinar o modelo
peso, bias, historico = treinar_modelo_completo(dados_treino, 0.1, 30, 0.0001, 10)

# 2. Avaliar o modelo
mse_treino, mse_teste = comparar_desempenho(dados_treino, dados_teste, peso, bias)

# 3. Mostrar os resultados
print("Peso aprendido:", peso)
print("Bias aprendido:", bias)
print("MSE inicial:", historico[0])
print("MSE final treino:", mse_treino)
print("MSE teste:", mse_teste)

assert mse_treino < historico[0]

assert abs(mse_treino - historico[-1]) < 1e-10

assert mse_teste > mse_treino
