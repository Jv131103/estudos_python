"""
Faça dois programas:

    Gere uma senha de 10 caracteres usando random.choice

    Gere uma senha de 10 caracteres usando secrets.choice

Depois:

    Compare as abordagens

    Pense em qual NÃO deve ser usada em produção
"""

import random
import secrets

CARACTERES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*:;.,/?|\\\"'+_-="


def gerar_senha_random(tam=10):
    return "".join([random.choice(CARACTERES) for _ in range(tam)])


def gerar_senha_secrets(tam=10):
    return "".join([secrets.choice(CARACTERES) for _ in range(tam)])


print(gerar_senha_random())
print(gerar_senha_secrets())
