"""
Crie um script que:

    Receba nome e idade via input

    Salve em usuario.json

    Formate com indent=4
"""

import json


def salvar_pessoa(**kwargs):
    with open("./jsons/usuario.json", "w", encoding="utf-8") as f:
        json.dump(kwargs, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salvar_pessoa(nome=nome, idade=idade)
