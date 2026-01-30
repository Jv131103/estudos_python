"""
Faça um programa que:

    Crie um arquivo log.txt

    Escreva 3 linhas iniciais

    Feche corretamente o arquivo

    Abra o mesmo arquivo novamente em modo append

    Adicione mais 2 linhas

    Leia e mostre o conteúdo final

DICAS

    Use dois blocos with

    Use \n corretamente

    Pense na diferença entre "w" e "a"
"""

import datetime


def create_file(name_file="./arquivos/log.txt"):
    with open(name_file, mode="w", encoding="utf-8") as file:
        file.writelines(
            [
                "[PROCEDIMENTO] CRIAÇÃO DE LOG\n",
                f"[INFO] CRIADO EM {datetime.datetime.today()}\n",
                "[CRIADOR] João Vitor Justino\n"
            ]
        )


def add_log(*messages, name_file="./arquivos/log.txt"):
    with open(name_file, "a", encoding="utf-8") as file:
        file.writelines(messages)


def read_log(name_file="./arquivos/log.txt"):
    with open(name_file, "r", encoding="utf-8") as file:
        print("=== CONTEÚDO FINAL DO LOG ===")
        for linha in file:
            print(linha.rstrip("\n"))


create_file()
add_log(
    "\n[PROCEDIMENTO] Adição de Logs\n"
    "[SUCCESS] dados adicionados em log\n",
    "[WARNING] teste de log sucedido mas sem utilização\n",
    "[SUCESS] log funcional\n"
)
read_log()
