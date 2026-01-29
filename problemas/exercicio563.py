"""
Faça dois programas:

    Um que use random.seed(123) e gere uma sequência

    Um que use secrets.randbelow

Depois:

    Execute várias vezes

    Compare os resultados

    Explique (em comentário) por que um é previsível e o outro não
"""

import random
import secrets


def gerar_random(limite):
    # random.seed(123)

    return random.randint(0, limite)


def gerar_secrets(limite):
    return secrets.randbelow(limite)


cont = 0

while cont < 5:
    print(f"Random: {gerar_random(10)}")
    print(f"Secrets: {gerar_secrets(10)}")
    cont += 1
