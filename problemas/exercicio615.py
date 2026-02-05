"""
Usar pathlib para listar todos os arquivos .py da pasta atual.

Regras

    Use Path

    Use glob

    Não pode usar os

O que o script deve fazer

    Pegar a pasta atual

    Listar todos os arquivos .py

    Imprimir apenas o nome do arquivo
"""

from pathlib import Path


def listdotpy(path):
    path = Path(path)

    if not path.exists():
        print("Path não encontrado")
        print("Pegando do dir atual")
        path = Path.cwd()

    files = path.glob('**/*.py')

    for py in files:
        if py.is_file() and "venv" not in py.parts:
            print(py.name)


listdotpy("./batata/")
