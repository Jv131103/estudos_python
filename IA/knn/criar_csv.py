import random
from pathlib import Path

import pandas as pd


PASTA = Path("./IA/knn")
PASTA.mkdir(parents=True, exist_ok=True)

CAMINHO_CSV = PASTA / "alunos.csv"

dados = {
    "horas_estudo": [],
    "faltas": [],
    "sono_horas": [],
    "participacao": [],
    "media_atividades": [],
    "aprovado": [],
}

for _ in range(1000):
    horas = random.randint(1, 12)
    faltas = random.randint(0, 20)
    sono = random.randint(3, 10)
    participacao = random.randint(0, 10)
    media_atividades = round(random.uniform(0, 10), 1)

    score = (
        horas * 0.8
        - faltas * 0.35
        + sono * 0.4
        + participacao * 0.5
        + media_atividades * 0.9
    )

    score += random.uniform(-3, 3)

    aprovado = 1 if score >= 11 else 0

    dados["horas_estudo"].append(horas)
    dados["faltas"].append(faltas)
    dados["sono_horas"].append(sono)
    dados["participacao"].append(participacao)
    dados["media_atividades"].append(media_atividades)
    dados["aprovado"].append(aprovado)

df = pd.DataFrame(dados)

df.to_csv(CAMINHO_CSV, index=False)

print("CSV criado com sucesso!")
print(f"Caminho: {CAMINHO_CSV}")
print()
print(df.head())
print()
print("Distribuição da variável aprovado:")
print(df["aprovado"].value_counts())
print()
print("Percentual:")
print(df["aprovado"].value_counts(normalize=True))
