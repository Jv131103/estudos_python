def contar_palavra_mais_frequente(texto):
    strings = texto.lower().split()

    dicionario = {}

    dicionario_analise = {}
    total_palavras = 0

    # Passo 1: contar cada string e quantas palavras existem no texto
    for string in strings:
        dicionario_analise[string] = dicionario_analise.get(string, 0) + 1
        total_palavras += 1


    # Passo 2: analisar qual a mais frequente
    mais_frequente = ""
    ocorrencias = 0

    for chave, valor in dicionario_analise.items():
        if valor > ocorrencias:
            ocorrencias = valor
            mais_frequente = chave

    dicionario['total_palavras'] = total_palavras
    dicionario['mais_frequente'] = mais_frequente
    dicionario['ocorrencias'] = ocorrencias

    return dicionario


texto = """Se eu moro em São Paulo, então eu moro no Brasil. Moro onde quiser"""
print(contar_palavra_mais_frequente(texto))
