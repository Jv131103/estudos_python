"""
Faça um programa que:

    imprime a pasta atual

    lista os arquivos nela

    cria uma pasta backup se não existir

(Módulos: os)
"""

import os

directory = os.getcwd()
print(f"Pasta atual: {directory}\n")

backup = "backup"
os.makedirs(backup, exist_ok=True)

IGNORAR = (".git", "venv", "databases")
EXTENSOES_REMOVER = (".pyc",)

for root, dirs, files in os.walk(directory):
    if any(pasta in root for pasta in IGNORAR):
        continue

    for file in files:
        if not file.endswith(EXTENSOES_REMOVER):
            print(os.path.join(root, file))
