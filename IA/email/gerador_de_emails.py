import random
from pathlib import Path

import pandas as pd
from faker import Faker

from pipeline import validar_email, extrair_features_email, FEATURES


QTD = 7000

PASTA = Path("./IA/email")
PASTA.mkdir(parents=True, exist_ok=True)

CAMINHO_CSV = PASTA / "emails.csv"

fake = Faker("pt_BR")


emails_validos_manuais = [
    "renato@gmail.com",
    "olamundo@gmail.com.br",
    "contato@empresa.com.br",
    "aluno@faculdade.edu.br",
    "maria.silva@hotmail.com",
    "joao_123@yahoo.com",
    "suporte@meusite.com",
    "cliente@loja.com.br",
    "professor@escola.edu.br",
    "vendas@empresa.com",
]


emails_invalidos_base = [
    "semarroba.com",
    "teste@@gmail.com",
    "@gmail.com",
    "joao@",
    "maria@gmail",
    "abc.com.br",
    "teste@.com",
    "teste@gmail..com",
    "teste gmail@gmail.com",
    "",
    "   ",
    "ana@com",
    "pedro@gmail.",
    "renato@",
    "usuario@dominio",
    "teste@teste.com",
    "teste@test.com",
    "usuario@example.com",
    "contato@fake.com",
    "qualquer@email.com",
]


dados = {
    "email": [],
}

for feature in FEATURES:
    dados[feature] = []

dados["valido"] = []


for i in range(QTD):
    if i < QTD // 2:
        if random.random() < 0.35:
            email = random.choice(emails_validos_manuais)
        else:
            email = fake.email()
    else:
        email = random.choice(emails_invalidos_base)

    email = str(email).strip().lower()

    features = extrair_features_email(email)
    valido = validar_email(email)

    dados["email"].append(email)

    for feature in FEATURES:
        dados[feature].append(features[feature])

    dados["valido"].append(valido)


df = pd.DataFrame(dados)

df = df.drop_duplicates(subset=["email"], keep="last")

df.to_csv(CAMINHO_CSV, index=False)

print("CSV criado com sucesso!")
print(CAMINHO_CSV)
print()
print(df.head())
print()
print("Distribuição:")
print(df["valido"].value_counts())
print()
print("Percentual:")
print(df["valido"].value_counts(normalize=True))
