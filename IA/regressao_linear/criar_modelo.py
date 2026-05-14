from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
import numpy as np
import pandas as pd


df = pd.read_csv("./IA/regressao_linear/notas.csv")

X = df[["horas_estudo"]]
Y = df["nota"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

modelo = LinearRegression()

# Treinar:
modelo.fit(X_train, y_train)

# Aprendizado:
print(modelo.coef_)  # quanto y sobe quando x sobe 1 unidade. EX: +1 hora → +1.2 nota
print(modelo.intercept_)  # Começo da reta. EX: Se: horas = 0, nota prevista: 1.8

# PREVER:
# EX: Se teste: [[5]], saída: [7.9]
y_pred = modelo.predict(X_test)
print(y_pred)

# Visão
# N: Horas
# M: O valor verdadeiro será esse
# O: O modelo achou isso
# P: Portanto o erro será, esse
# Significado: Para N horas o valor verdadeiro será M e o modelo achou O, ou seja, o erro é de M - O = P
# erro positivo: 0.1 - modelo previu MENOR, Porque: M > O
# erro negativo: -0.1 - modelo previu MAIOR, Porque: O > M
resultado = pd.DataFrame({
    "horas_estudo": X_test["horas_estudo"],
    "real": y_test,
    "previsto": y_pred,
})
resultado["erro"] = resultado["real"] - resultado["previsto"]
# print(resultado)
# Erro absoluto
resultado["erro_abs"] = abs(resultado["erro"])

print(resultado)


# Métrica 1:
# Erro absoluto médio.
mae = mean_absolute_error(y_test, y_pred)
print(mae)  # em média erra N ponto.

# MÉTRICA 2 — MSE:
# Erro quadrático médio.
mse = mean_squared_error(y_test, y_pred)
print(mse)  # Erro grande dói mais. Porque quadrado. EX Erro: 2 → 4

# MÉTRICA 3 — RMSE
# Raiz do MSE.
# Volta para unidade original.
rmse = np.sqrt(mse)
print(rmse)

# MÉTRICA 4 — R²
r2 = r2_score(y_test, y_pred)
print(r2)  # Interpretação: 0.0 = lixo | 1.0 = perfeito. Se 0.92, modelo explica 92% da variação.
