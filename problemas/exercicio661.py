"""
Criar um script que:

Compacte todos os arquivos .txt da pasta atual

Ignore:

    pastas venv

    pastas .git

    O nome do ZIP deve ser:

        backup_txt_YYYYMMDD.zip


Use compressão ZIP_DEFLATED

Regras:

    Use pathlib

    Use zipfile

    Use datetime

Não use shutil.make_archive
"""

import zipfile as zp
from datetime import datetime
from pathlib import Path


class CompactExtension:
    def __init__(self, dir=".", type_file="txt") -> None:
        self.dir = Path(dir)
        self.type_file = type_file
        self.data = datetime.now().strftime("%Y%m%d")
        self.name_backup = f"backup_{self.type_file}_{self.data}.zip"

    def compact(self):
        all_files = self.dir.rglob(f"*.{self.type_file}")
        tot_files = 0

        with zp.ZipFile(self.name_backup, "w", compression=zp.ZIP_DEFLATED) as zp_compact:
            for arquivo in all_files:
                if any(p in (".git", "venv", "__pycache__") for p in arquivo.parts):
                    continue

                if arquivo.is_file():
                    zp_compact.write(arquivo, arquivo.relative_to(self.dir))
                    tot_files += 1

        print(f"TOTAL DE ARQUIVOS COMPACTADOS: {tot_files}")

        zip_size_bytes = Path(self.name_backup).stat().st_size
        print("TAMANHO FINAL DO ZIP:", self._formatar_tamanho(zip_size_bytes))

    def _formatar_tamanho(self, tamanho_bytes):
        for unidade in ["B", "KB", "MB", "GB"]:
            if tamanho_bytes < 1024:
                return f"{tamanho_bytes:.2f} {unidade}"
            tamanho_bytes /= 1024
        return f"{tamanho_bytes:.2f} TB"


if __name__ == "__main__":
    compactar = CompactExtension(type_file="txt")
    compactar.compact()
