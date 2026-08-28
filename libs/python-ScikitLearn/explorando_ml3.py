import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

dados = {
    "horas_sono": [4, 6, 8, 5, 7, 3, 9, 6, 8, 4],
    "horas_estudo": [2, 4, 6, 3, 5, 1, 7, 4, 6, 2],
    "passou": [0, 1, 1, 0, 1, 0, 1, 1, 1, 0]
}

df = pd.DataFrame(dados)
print(df)

# Tratamento
print("Tratando Valores nulos...")
df["horas_sono"] = df["horas_sono"].fillna(0)
df["horas_estudo"] = df["horas_estudo"].fillna(0)
df["passou"] = df["passou"].fillna(0)

print("Separando X e Y...")
X = df[['horas_sono', "horas_estudo"]]
y = df["passou"]

print("Iniciando o treino...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Total de registros: {len(X)}")
print(f"Registros de treino (80%): {len(X_train)}")
print(f"Registros de teste (20%): {len(X_test)}")
print()

print("Criando o modelo...")
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)
print("REALIZANDO PREVISÃO...")
previsoes = modelo.predict(X_test)
print("Previsão retornada:", previsoes)
print()

acuracia = accuracy_score(y_test, previsoes)
print("Acurácia:", acuracia)
print()
