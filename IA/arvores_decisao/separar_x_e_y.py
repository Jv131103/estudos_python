import pandas as pd

df = pd.read_csv("./IA/arvores_decisao/alunos.csv")

X = df[["horas_estudo", "faltas", "sono_horas"]]
y = df["aprovado"]

print(X)
print()
print(y)
