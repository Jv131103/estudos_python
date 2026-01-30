"""
Ler arquivo linha por linha

Faça um programa que:

    Leia um arquivo de texto chamado dados.txt

    Imprima cada linha do arquivo

    Remova o \n do final de cada linha

DICAS

    Use with

    Use o arquivo como iterador

    Use strip() ou rstrip("\n")
"""


def ler_arquivo(archive , encoding="utf-8"):
    with open(archive, "r", encoding=encoding) as file:
        print("Lendo arquivos ...")

        for dados in file.readlines():
            print(dados.rstrip("\n"))


ler_arquivo("./arquivos/dados.txt")
