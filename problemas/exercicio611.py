"""
Crie um .env com:

    DATABASE_URL=postgresql://user:senha@localhost:5432/meubanco
    SECRET_KEY=minha_chavinha_secreta
    TIMEOUT=30

Crie um script que:

    . carregue o .env

    . valide se DATABASE_URL e SECRET_KEY existem

        . se não existirem, levante ValueError

    . leia TIMEOUT como inteiro

    . imprima apenas:

        Configurações carregadas com sucesso

    . não imprima valores sensíveis (SECRET_KEY, DATABASE_URL)

Dica profissional:

    Nunca faça print de secrets em produção.
"""

import os

from dotenv import load_dotenv

load_dotenv()  # carrega o .env

required_vars = ["DATABASE_URL", "SECRET_KEY"]

for var in required_vars:
    if not os.getenv(var):
        raise ValueError(f"Variável de ambiente {var} não configurada")

timeout = int(os.getenv("TIMEOUT", 0))

print("Configurações carregadas com sucesso")
