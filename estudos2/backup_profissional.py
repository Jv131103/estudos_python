import zipfile
from datetime import datetime
from pathlib import Path

data = datetime.now().strftime("%Y%m%d_%H%M%S")
nome_backup = f"backup_{data}.zip"

with zipfile.ZipFile(
    nome_backup,
    "w",
    compression=zipfile.ZIP_DEFLATED
) as z:
    for arquivo in Path.cwd().rglob("*"):
        if ".git" in arquivo.parts or "venv" in arquivo.parts or "__pycache__" in arquivo.parts:
            continue
        if arquivo.is_file():
            print(f"Arquivo: {arquivo}")
            z.write(arquivo)    

print("Backup criado:", nome_backup)
