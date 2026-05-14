import pandas as pd

df = pd.read_csv("./IA/regressao_logistica/alunos.csv")

X = df[["horas_estudo", "faltas"]]
y = df["aprovado"]

print(X)
print()
print(y)
