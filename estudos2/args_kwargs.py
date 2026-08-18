def estatisticas_flex(*numeros, **opcoes):
    if not numeros:
        return {}

    dados = {}

    if opcoes.get("incluir_soma", True):
        dados['soma'] = sum(numeros)

    if opcoes.get("incluir_media", True):
        dados['media'] = sum(numeros) / len(numeros)

    return dados


print(estatisticas_flex(4, 8, 15, 16, 23, 42))
print(estatisticas_flex(1, 2, 3, incluir_media=False))
print(estatisticas_flex())
