"""
Faça um script que:

    recebe por sys.argv o nome de uma pasta

    copia essa pasta para NOME_backup usando shutil.copytree

(Módulos: sys, shutil)
"""

import os
import shutil
import sys

if len(sys.argv) < 2:
    print("Uso: python exercicio607.py NOME_DA_PASTA")
    sys.exit(1)

pasta_origem = sys.argv[1]
pasta_backup = pasta_origem + "_backup"

if not os.path.isdir(pasta_origem):
    print("A pasta informada não existe.")
    sys.exit(1)

shutil.copytree(pasta_origem, pasta_backup, dirs_exist_ok=True)

print("Backup criado com sucesso.")
