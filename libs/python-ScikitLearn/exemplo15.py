# Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

CAMINHO_DATASET = "./libs/python-ScikitLearn/galton.csv"


# Ler o dataset
df = pd.read_csv(CAMINHO_DATASET)

print(df.head(5))
print()
print(df.info())
print()


# Remover linhas duplicadas
df.drop_duplicates(inplace=True)


# Remover colunas inúteis para o problema
df.drop(columns=["family", "children", "childNum"], inplace=True)


# Converter polegadas para metros
def inch2m(inch):
    return inch * 2.54 / 100


for coluna in ["father", "mother", "midparentHeight", "childHeight"]:
    df[coluna] = df[coluna].apply(inch2m)


# Converter gender de texto para número
df["gender"] = df["gender"].apply(lambda x: 0 if x == "male" else 1)


# Criar coluna com a média da altura dos pais
df["media"] = (df["father"] + df["mother"]) / 2


# Exibir amostra
print(df.sample(5))
print()


# =====================================================
# REGRESSÃO LINEAR SIMPLES
# Usando apenas a média da altura dos pais
# =====================================================

X = np.array(df["media"]).reshape(-1, 1)
y = df["childHeight"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


reta = LinearRegression()
reta.fit(X_train, y_train)

y_pred = reta.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("Regressão Linear Simples")
print(f"MSE = {mse}")
print(f"MAE = {mae}")
print(f"R² = {r2}")
print()


# Gráfico da regressão simples
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color="red")

plt.title("Regressão da altura média dos pais e dos filhos")
plt.xlabel("Altura média dos pais (m)")
plt.ylabel("Altura dos filhos (m)")

plt.show()


# =====================================================
# REGRESSÃO LINEAR MÚLTIPLA
# Usando várias colunas como entrada
# =====================================================

X = df.drop(columns=["childHeight", "midparentHeight"])
y = df["childHeight"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# Padronização dos dados
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


reta2 = LinearRegression()
reta2.fit(X_train_scaled, y_train)

y_pred = reta2.predict(X_test_scaled)


mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print("Regressão Linear Múltipla")
print(f"MSE = {mse}")
print(f"MAE = {mae}")
print(f"R² = {r2}")
print()


# Intercepto
print("Intercept:", reta2.intercept_)


# Coeficientes
coeficientes = pd.DataFrame({
    "features": X_train.columns,
    "coeficientes": reta2.coef_
})

print(coeficientes)
