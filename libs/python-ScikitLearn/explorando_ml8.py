import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

dados_scaling = {
    "idade": [22, 25, 47, 52, 46, 56, 23, 24, 21, 34],
    "salario": [15000, 18000, 90000, 100000, 85000, 120000, 16000, 17000, 14000, 40000],
    "comprou": [0, 0, 1, 1, 1, 1, 0, 0, 0, 1]
}

df = pd.DataFrame(dados_scaling)
print(df)
print()

X = df[["idade", "salario"]]
y = df['comprou']

# 1. Separar treino e teste PRIMEIRO
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Scaler: fit SÓ no treino, transform nos dois
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # aprende média/desvio do treino
X_test_scaled = scaler.transform(X_test)        # só aplica, não recalcula

# 3. Treinar o modelo com dados de treino escalonados
knc = KNeighborsClassifier(n_neighbors=3)
knc.fit(X_train_scaled, y_train)

# 4. Prever nos dados de TESTE (nunca vistos pelo modelo)
y_pred = knc.predict(X_test_scaled)

# 5. Avaliar com dados de teste (medida confiável)
acuracia = accuracy_score(y_test, y_pred)
print(f"Acurácia do KNN com StandardScaler: {acuracia:.2%}")
