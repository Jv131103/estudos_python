"""
Criar um programa que:

Pergunte:

    nome

    idade

    email

"""

import json
from pathlib import Path

CAMINHO = Path("./jsons/usuarios.json")


def ler_int(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            return int(valor)
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")


def ler_email(mensagem):
    while True:
        email = input(mensagem).strip()
        if "@" in email and "." in email:
            return email
        print("Email inválido. Tente de novo.")


def garantir_arquivo():
    CAMINHO.parent.mkdir(parents=True, exist_ok=True)
    if not CAMINHO.exists():
        CAMINHO.write_text("[]", encoding="utf-8")


def ler_usuarios():
    garantir_arquivo()
    with open(CAMINHO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    if not isinstance(dados, list):
        dados = []

    return dados


def adicionar_no_json(dados, **kwargs):
    dados.append(kwargs)

    with open(CAMINHO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print("USUARIO ADICIONADO COM SUCESSO!")


def salvar_usuario(nome, idade, email):
    usuarios = ler_usuarios()
    adicionar_no_json(usuarios, nome=nome, idade=idade, email=email)


if __name__ == "__main__":
    while True:
        nome = input("Nome: ")
        idade = ler_int("Idade: ")
        email = ler_email("Email: ")

        print(f"Cadastrando {nome}")

        salvar_usuario(nome, idade, email)

        de_novo = input("Cadastrar outro usuário? [SIM/NAO] ").strip().upper()
        if de_novo != "SIM":
            break
