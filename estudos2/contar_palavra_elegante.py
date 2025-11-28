def contar_palavra_mais_frequente(texto):
    palavras = texto.lower().split()
    contagem = {}

    for p in palavras:
        contagem[p] = contagem.get(p, 0) + 1

    mais_frequente = max(contagem, key=contagem.get)  # type: ignore
    ocorrencias = contagem[mais_frequente]

    return {
        "total_palavras": len(palavras),
        "mais_frequente": mais_frequente,
        "ocorrencias": ocorrencias
    }


texto = """Se eu moro em São Paulo, então eu moro no Brasil. Moro onde quiser"""
print(contar_palavra_mais_frequente(texto))
