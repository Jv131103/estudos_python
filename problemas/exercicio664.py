"""
Crie um script que:

    Leia usuario.json

    Adicione campo "ativo": true

    Salve novamente
"""

import json

from exercicio663 import salvar_pessoa


def ler_usuario():
    with open("./jsons/usuario.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    return dados


if __name__ == "__main__":
    d_user = ler_usuario()
    d_user["ativo"] = True
    salvar_pessoa(**d_user)
