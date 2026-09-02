import json
from datetime import datetime
from pathlib import Path

from filelock import FileLock

FILES = Path().cwd() / "jsons" / "eventos.json"
LOCK_PATH = str(FILES) + ".lock"


def registrar_evento(caminho_arquivo, tipo, mensagem):
    lock = FileLock(LOCK_PATH, timeout=5)
    with lock:
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            try:
                valores = json.load(file)
            except json.decoder.JSONDecodeError:
                valores = []

        valores.append({
            "tipo": tipo,
            "mensagem": mensagem,
            "timestamp": datetime.now().isoformat()  # <- valor de verdade, não "..."
        })

        with open(caminho_arquivo, "w", encoding="utf-8") as file:
            json.dump(valores, file, indent=4, ensure_ascii=False)


def resumo_por_tipo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        try:
            valores = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            valores = []

        novo = {}

        for d in valores:
            novo[d['tipo']] = novo.get(d['tipo'], 0) + 1

        return novo


registrar_evento(FILES, "erro", "Falha ao conectar")
registrar_evento(FILES, "info", "Sistema iniciado")
registrar_evento(FILES, "erro", "Timeout na API")

print(resumo_por_tipo(FILES))
