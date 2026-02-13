"""
Agora vamos para algo mais profissional.

Criar um script que:

    Recebe o nome de um arquivo ZIP via sys.argv

    Extrai para uma pasta chamada:

        extraido_nome_do_zip

    Antes de extrair:

        Verifica se o ZIP existe

        Lista os arquivos contidos nele

    Extrai com segurança (evitar path traversal básico)

Regras:

    Use pathlib

    Use zipfile

    Use sys

    Não use extractall() direto sem verificação

"""
import sys
import zipfile
from pathlib import Path


def safe_extract(zip_path: Path, dest_dir: Path) -> None:
    """
    Extrai zip com verificação básica contra path traversal:
    - bloqueia caminhos absolutos
    - bloqueia '..' que escapem da pasta destino
    """
    dest_dir.mkdir(parents=True, exist_ok=True)
    base = dest_dir.resolve()

    with zipfile.ZipFile(zip_path, "r") as z:
        # 1) listar conteúdo
        print("Arquivos no ZIP:")
        for name in z.namelist():
            print(" -", name)

        # 2) extrair item por item com validação
        for info in z.infolist():
            name = info.filename

            # ignora entradas vazias estranhas
            if not name:
                continue

            # monta destino final
            target = (dest_dir / name)

            # resolve e valida se fica dentro do diretório base
            try:
                target_resolved = target.resolve()
                target_resolved.relative_to(base)  # se não for "filho", levanta ValueError
            except Exception:
                raise PermissionError(f"Entrada maliciosa detectada no ZIP: {name}")

            # se for diretório, cria e continua
            if name.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
                continue

            # garante pasta pai
            target.parent.mkdir(parents=True, exist_ok=True)

            # extrai por stream (sem extractall)
            with z.open(info, "r") as src, open(target, "wb") as dst:
                dst.write(src.read())


def main() -> int:
    if len(sys.argv) < 2:
        print("Uso: python extrair_zip.py arquivo.zip")
        return 2

    zip_path = Path(sys.argv[1])

    if not zip_path.exists() or not zip_path.is_file():
        print("Erro: ZIP não existe ou não é arquivo:", zip_path)
        return 2

    if zip_path.suffix.lower() != ".zip":
        print("Aviso: arquivo não termina com .zip, mas vou tentar abrir mesmo.")

    if not zipfile.is_zipfile(zip_path):
        print("Erro: arquivo não é um ZIP válido:", zip_path)
        return 2

    dest_dir = Path(f"extraido_{zip_path.stem}")

    try:
        safe_extract(zip_path, dest_dir)
        print(f"\nExtração concluída em: {dest_dir.resolve()}")
        return 0
    except Exception as e:
        print("Erro ao extrair:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
