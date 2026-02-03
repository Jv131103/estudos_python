"""
Crie um .env com:

    DEBUG=True
    PORT=8000
    APP_NAME=MinhaAplicacao

Crie um script que:

    carregue o .env

    leia as variáveis

    converta DEBUG para bool

    converta PORT para int

    imprima:

        Aplicação: MinhaAplicacao
        Rodando na porta: 8000
        Modo debug: ativo

Dica extra

    Lembre que os.getenv() sempre retorna string
"""

import os

from dotenv import load_dotenv

load_dotenv()

app = os.getenv("APP_NAME", "APP ZERADO")
porta = int(os.getenv("PORT", 0))
debug = os.getenv("DEBUG", "").lower() == "true"

status_debug = "ativo" if debug else "desativado"

print(f"Aplicação: {app}")
print(f"Rodando na porta: {porta}")
print(f"Modo debug: {status_debug}")
