"""
Faça um programa que:

    . Leia dois valores booleanos:

        . está_logado
        . é_admin

    . Use uma tabela de decisão

    . Retorne:

        "Acesso total"

        "Acesso limitado"

        "Acesso negado"

Não use if/elif.
"""


def versao_entrada_de_user():
    status_log = input("Está Logado? [y/n] ").strip().lower()
    esta_logado = True if status_log == "y" else False

    status_admin = input("É admin? [y/n] ").strip().lower()
    eh_admin = True if status_admin == "y" else False

    return esta_logado, eh_admin


def versao_entrada_aleatoria():
    from random import randint
    return randint(0, 1), randint(0, 1)  # 0, 1 apenas para fins didáticos sobre funcionamento de booleanos


def verificar_acesso(log=(False, False)):
    acesso = {
        (True, True): "Acesso total",
        (False, False): "Acesso negado",
    }

    return acesso.get(log, "Acesso limitado")


status_log = versao_entrada_de_user()
print(f"Status do usuário em modo input: {verificar_acesso(status_log)}")

status_log2 = versao_entrada_aleatoria()
print(f"Status do usuário em modo aleatório: {verificar_acesso(status_log2)}")
