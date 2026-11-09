def analisar_logins(tentativas):
    tabela = {
        "ERRO": "falhas",
        "OK": "sucessos",
    }

    resultado = {
        "sucessos": 0,
        "falhas": 0,
        "ignoradas": 0,
        "bloqueado": False,
        "indice_bloqueio": None
    }

    erros_consecutivos = 0

    for idx, tentativa in enumerate(tentativas):
        categoria = tabela[tentativa]

        # Conta todos os OK e ERRO recebidos
        resultado[categoria] += 1

        # Após o bloqueio, não altera mais o estado
        if resultado["bloqueado"]:
            resultado["ignoradas"] += 1
            continue

        if tentativa == "ERRO":
            erros_consecutivos += 1

            if erros_consecutivos >= 3:
                resultado["bloqueado"] = True
                resultado["indice_bloqueio"] = idx

        else:
            erros_consecutivos = 0

    return resultado


tentativas = [
    "ERRO", "ERRO", "OK",
    "ERRO", "ERRO", "ERRO",
    "OK", "ERRO"
]
print(analisar_logins(tentativas))

tentativas = ["ERRO", "OK", "ERRO", "OK", "ERRO"]
print(analisar_logins(tentativas))
