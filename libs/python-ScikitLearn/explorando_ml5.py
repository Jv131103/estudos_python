import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

dados_carros = {
    "ano": [2015, 2018, 2020, 2016, 2022, 2019, 2014, 2021],
    "km_rodado": [80000, 40000, 15000, 70000, 5000, 30000, 95000, 10000],
    "preco": [35000, 55000, 75000, 40000, 95000, 60000, 30000, 85000]
}

df = pd.DataFrame(dados_carros)
print(df)

print("Tratando Valores nulos...")
df["ano"] = df["ano"].fillna(df["ano"].median())
df["km_rodado"] = df["km_rodado"].fillna(
    df.groupby("ano")["km_rodado"].transform("median")
)
df["preco"] = df["preco"].fillna(
    df.groupby("ano")["preco"].transform("median")
)

# Separando X e y
X = df[["ano", "km_rodado"]]  # Colchetes duplos mantêm como DataFrame
y = df["preco"]  # Colchete simples cria uma Series

print("Iniciando o treino...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Total de registros: {len(X)}")
print(f"Registros de treino (80%): {len(X_train)}")
print(f"Registros de teste (20%): {len(X_test)}")
print()

print("Criando o modelo...")
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Realizando previsão antes de adicionar novo carro
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

# Testando o carro (Ano: 2020, Km: 50.000)
# A ordem das colunas no teste DEVE ser a mesma do X: ["ano", "km_rodado"]
carro_teste = pd.DataFrame([[2020, 50000]], columns=["ano", "km_rodado"])

preco_previsto = modelo.predict(carro_teste)
print(f"Preço estimado: R$ {preco_previsto[0]:.2f}")
