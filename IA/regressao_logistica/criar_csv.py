import pandas as pd
import random

dados = {
    "horas_estudo": [],
    "faltas": [],
    "aprovado": [],
}

for _ in range(1000):
    horas = random.randint(1, 12)
    faltas = random.randint(0, 20)

    score = horas - (faltas * 0.4)

    ruido = random.uniform(-2, 2)

    score += ruido

    aprovado = 1 if score >= 4 else 0

    dados["horas_estudo"].append(horas)
    dados["faltas"].append(faltas)
    dados["aprovado"].append(aprovado)

df = pd.DataFrame(dados)

df.to_csv("./IA/regressao_logistica/alunos.csv", index=False)

print(df.head())
