import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("PARTE 1")
# Criando o DataFrame
dados = {
    'Horas_Estudo_X': [1.5, 2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 10.0],
    'Nota_Prova_Y': [4.5, 5.0, 6.0, 6.5, 7.0, 8.0, 8.5, 9.0, 9.2, 9.8]
}

df = pd.DataFrame(dados)
print(df)

# Tratamento
print("Tratando Valores nulos...")
df["Horas_Estudo_X"] = df["Horas_Estudo_X"].fillna(0)
df["Nota_Prova_Y"] = df["Nota_Prova_Y"].fillna(0)

print("Separando X e Y...")
X = df[['Horas_Estudo_X']]
y = df["Nota_Prova_Y"]

print("Iniciando o treino...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Total de registros: {len(X)}")
print(f"Registros de treino (80%): {len(X_train)}")
print(f"Registros de teste (20%): {len(X_test)}")
print()

print("Criando o modelo...")
modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("REALIZANDO PREVISÃO...")
previsoes = modelo.predict(X_test)
print("Previsão retornada:", previsoes)
print()
erro = mean_squared_error(y_test, previsoes)
print("Erro:", erro)
print()
r2 = r2_score(y_test, previsoes)
print("Coeficiente de Determinação (R²):", r2)

print()
print("PARTE 2")
dados = {
    'Horas_Sono': [3.0, 4.0, 4.5, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 9.0],
    'Passou': [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
}
df = pd.DataFrame(dados)

# 2. Definição das variáveis (X com colchetes duplos!)
X = df[['Horas_Sono']]  # DataFrame 2D
y = df['Passou']        # Series 1D

# Tratamento
print("Tratando Valores nulos...")
df["Horas_Sono"] = df["Horas_Sono"].fillna(0)
df["Passou"] = df["Passou"].fillna(0)

print("Separando X e Y...")
X = df[['Horas_Sono']]
y = df["Passou"]

print("Iniciando o treino...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Total de registros: {len(X)}")
print(f"Registros de treino (80%): {len(X_train)}")
print(f"Registros de teste (20%): {len(X_test)}")
print()

print("Criando o modelo...")
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)
print("REALIZANDO PREVISÃO...")
previsoes = modelo.predict(X_test)
print("Previsão retornada:", previsoes)
print()

acuracia = accuracy_score(y_test, previsoes)
print("Acurácia:", acuracia)
print()
