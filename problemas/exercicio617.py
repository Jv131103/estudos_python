"""
Organizar arquivos por extensão usando pathlib.

Cenário real

    Na pasta downloads/ existem arquivos misturados:

        .pdf

        .jpg

        .png

        .zip

    O que o script deve fazer

        Percorrer todos os arquivos da pasta

        Criar uma pasta com o nome da extensão (ex: pdf/, jpg/)

        Mover os arquivos para a pasta correta

    Regras

        Use Path

        Use glob

        Use mkdir(exist_ok=True)

        Use rename() ou replace()
"""
from pathlib import Path


def organizar_por_extensao(caminho):
    base = Path(caminho)

    for p in base.glob("*"):  # só a pasta, não precisa recursivo
        if not p.is_file():
            continue

        ext = p.suffix.lower().lstrip(".")
        if not ext:  # arquivo sem extensão
            continue

        destino_dir = base / ext
        destino_dir.mkdir(exist_ok=True)

        destino = destino_dir / p.name
        p.replace(destino)

        print(f"OK → {p.name} -> {destino_dir.name}/")


organizar_por_extensao("/home/debianjv/Downloads/")
