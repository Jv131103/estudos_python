"""
Criar um programa que:

    Leia usuarios.json

Mostre:

    Quantidade total de usuários

    Média de idade

    Nome do usuário mais velho

Mostre tudo formatado no terminal
"""

from exercicio665 import ler_usuarios

USUARIOS = ler_usuarios()


def retornar_total_de_usuarios():
    return len(USUARIOS)


def media_de_idade():
    if not retornar_total_de_usuarios():
        return 0
    return sum([usuario["idade"] for usuario in USUARIOS]) / retornar_total_de_usuarios()


def usuario_mais_velho():
    if not USUARIOS:
        return "Nenhum usuário cadastrado"

    maior_idade = USUARIOS[0]['idade']
    nome = USUARIOS[0]["nome"]

    for dados in USUARIOS:
        if dados["idade"] > maior_idade:
            nome = dados["nome"]
            maior_idade = dados["idade"]

    return f"{nome} ({maior_idade} anos)"


def usuario_mais_velho_pythonico():
    if not USUARIOS:
        return "Nenhum usuário cadastrado"

    mais_velho = max(USUARIOS, key=lambda u: u["idade"])
    return f"{mais_velho['nome']} ({mais_velho['idade']} anos)"


print(f"Total de usuários: {retornar_total_de_usuarios()}")
print(f"Média: {media_de_idade()}")
print(f"Usuário mais velho: {usuario_mais_velho_pythonico()}")
