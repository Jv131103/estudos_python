from datetime import datetime
from pathlib import Path

DIARIO = Path().cwd() / "arquivos" / "diario.txt"


def adicionar_entrada(texto):
    with open(DIARIO, "a+", encoding="utf-8") as arq:
        arq.write(f"[{datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")}] {texto}\n")


def ler_entradas():
    with open(DIARIO, "r", encoding="utf-8") as arq:
        textos = arq.readlines()
        for texto in textos:
            print(texto, end="")


def contar_entradas():
    with open(DIARIO, "r", encoding="utf-8") as arq:
        return len(arq.readlines())


def limpar():
    with open(DIARIO, "w", encoding="utf-8"):
        return


limpar()

adicionar_entrada("Hoje foi um ótimo dia!")
adicionar_entrada("Aprendi sobre arquivos em Python.")

ler_entradas()

print(contar_entradas())
