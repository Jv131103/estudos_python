import pandas as pd
import random

dados = {
    "horas_estudo": [],
    "faltas": [],
    "sono_horas": [],
    "aprovado": [],
}

for _ in range(1000):
    horas = random.randint(1, 12)
    faltas = random.randint(0, 20)
    sono = random.randint(3, 10)

    score = 0

    # regra escondida do mundo
    if horas >= 6:
        score += 2

    if faltas <= 5:
        score += 2

    if sono >= 6:
        score += 1

    # ruído
    score += random.choice([-1, 0, 1])

    aprovado = 1 if score >= 3 else 0

    dados["horas_estudo"].append(horas)
    dados["faltas"].append(faltas)
    dados["sono_horas"].append(sono)
    dados["aprovado"].append(aprovado)

df = pd.DataFrame(dados)

df.to_csv("./IA/arvores_decisao/alunos.csv", index=False)

print(df.head())
