"""
Faça um programa que:

Gere um token seguro para um usuário

Use secrets.token_urlsafe

Armazene o token em um dicionário:

    usuario → token

Mostre o resultado
"""

import secrets


def generate_token_url(usuario):
    return {usuario: secrets.token_urlsafe()}


print(generate_token_url("JvJ"))
