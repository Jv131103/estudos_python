import pandas as pd
import random

dados = {
    "horas_estudo": [],
    "nota": []
}

for _ in range(1000):
    horas = random.randint(1, 12)

    ruido = random.randint(-2, 2)

    nota = (horas * 1.5) + ruido

    nota = max(0, min(10, nota))

    dados["horas_estudo"].append(horas)
    dados["nota"].append(round(nota, 1))

df = pd.DataFrame(dados)

df.to_csv("./IA/regressao_linear/notas.csv", index=False)

print(df.head())
