import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("./IA/regressao_logistica/alunos.csv")

X = df[["horas_estudo", "faltas"]]
y = df["aprovado"]

print(X)
print()
print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(X_train)
