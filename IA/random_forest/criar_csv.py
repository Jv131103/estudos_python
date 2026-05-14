import pandas as pd
import random
from pathlib import Path


# =========================
# CONFIGURAÇÕES
# =========================
PASTA = Path("./IA/random_forest")
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

    score = 0

    # Regras escondidas do negócio
    if horas >= 6:
        score += 2

    if faltas <= 5:
        score += 2

    if sono >= 6:
        score += 1

    if participacao >= 6:
        score += 1

    if media_atividades >= 6:
        score += 2

    # Ruído para simular mundo real
    score += random.choice([-2, -1, 0, 1, 2])

    aprovado = 1 if score >= 5 else 0

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
