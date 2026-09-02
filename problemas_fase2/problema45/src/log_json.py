import json
from datetime import datetime


def registrar_evento(caminho_arquivo, tipo, mensagem):
    # ATENÇÃO: esse padrão de ler-modificar-escrever NÃO é seguro em concorrência.
    # Se duas chamadas rodarem "ao mesmo tempo", ambas podem ler o arquivo
    # com o mesmo conteúdo inicial, e a segunda escrita sobrescreve a primeira,
    # perdendo o evento que foi registrado por ela. Isso é uma "race condition" —
    # o mesmo tipo de problema que bancos de dados resolvem com locks/transações.
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            valores = json.load(file)
    except FileNotFoundError:
        valores = []
    except json.decoder.JSONDecodeError:
        print(f"AVISO: '{caminho_arquivo}' continha JSON inválido — recriando do zero. Dados anteriores foram perdidos.")
        valores = []

    dados = {
        "tipo": tipo,
        "mensagem": mensagem,
        "timestamp": datetime.now().isoformat()
    }
    valores.append(dados)

    with open(caminho_arquivo, mode="w", encoding="utf-8") as file:
        json.dump(valores, file, indent=4, ensure_ascii=False)


def resumo_por_tipo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            valores = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        valores = []

    novo = {}
    for d in valores:
        novo[d['tipo']] = novo.get(d['tipo'], 0) + 1

    return novo
