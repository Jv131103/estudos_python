import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 1. Estrutura de dados original
dados = {
    "cidade": ["SP", "RJ", "SP", "MG", "RJ"],
    "idade": [25, 30, 22, 40, 35],
    "comprou": [1, 0, 1, 0, 1]
}

df = pd.DataFrame(dados)
print("DataFrame original:")
print(df)
print()

# 2. Encoding da variável categórica 'cidade'
# Transforma texto em colunas numéricas (0 ou 1) — modelos não entendem texto
df_encoded = pd.get_dummies(df, columns=["cidade"])
print("DataFrame após encoding (cidade virou colunas numéricas):")
print(df_encoded)
print()

# 3. Separação das variáveis explicativas (X) e do alvo (y)
X = df_encoded.drop(columns=['comprou'])  # tudo, menos a coluna que queremos prever
y = df_encoded['comprou']                  # a resposta certa (0 ou 1)

# 4. Separar em treino e teste
# IMPORTANTE: nunca avaliar o modelo com os mesmos dados usados no treino!
# Isso evita "vazamento de dados" e dá uma medida real de generalização.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Total de registros: {len(X)}")
print(f"Registros de treino (80%): {len(X_train)}")
print(f"Registros de teste (20%): {len(X_test)}")
print()

# 5. Treinamento da Regressão Logística
# O modelo aprende SÓ com os dados de treino
model = LogisticRegression()
model.fit(X_train, y_train)

# 6. Previsão nos dados de TESTE (que o modelo nunca viu)
y_pred = model.predict(X_test)
print("Previsões:", list(y_pred))
print("Valores reais:", list(y_test))
print()

# 7. Cálculo da acurácia — agora é uma medida confiável de performance
acuracia = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acuracia:.2%}")
