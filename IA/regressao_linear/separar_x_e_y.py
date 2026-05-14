import pandas as pd

df = pd.read_csv("./IA/regressao_linear/notas.csv")

X = df[["horas_estudo"]]
Y = df["nota"]

print(X)
print()
print(Y)
