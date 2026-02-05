"""
Encontrar todos os arquivos .txt dentro de uma pasta e subpastas.

    Regras

        Use pathlib

        Use rglob

    Ignore pastas chamadas:

        .git

        venv

    O que o script deve fazer

        Receber um caminho base

        Procurar todos os .txt

        Imprimir o caminho completo do arquivo
"""

from pathlib import Path


def list_all_txt_files(base_path):
    base_path = Path(base_path)

    for txt in base_path.rglob("*.txt"):
        if (
            txt.is_file()
            and "venv" not in txt.parts
            and ".git" not in txt.parts
        ):
            print(txt)


list_all_txt_files(".")
