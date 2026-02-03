"""
Crie um arquivo .env com:

    NOME=JOAO
    IDADE=22

Crie um script Python que:

    . carregue o .env
    . leia as variáveis NOME e IDADE
    . imprima:

        Nome: Renato
        Idade: 30

    Dicas

        Use load_dotenv()

        Use os.getenv()
"""

import os

from dotenv import load_dotenv

load_dotenv()  # carrega o .env

nome = os.getenv("NOME", "SEM NOME")
idade = os.getenv("IDADE", "IDADE NÃO DEFINIDA")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
