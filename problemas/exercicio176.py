import string
from pprint import pprint


def analisar_texto(texto):
    texto = texto.lower()
    text_editado = "".join([i for i in texto if i not in string.punctuation])
    texto_quebrado = text_editado.split()

    total_palavras = len(texto_quebrado)
    total_letra = 0
    for letra in texto_quebrado:
        for _ in letra:
            total_letra += 1

    frequencia_palavras = {}
    for p in texto_quebrado:
        frequencia_palavras[p] = frequencia_palavras.get(p, 0) + 1

    mais_frequente = max(frequencia_palavras, key=frequencia_palavras.get)  # type: ignore
    ocorrencias = frequencia_palavras[mais_frequente]

    return {
        "total_palavras": total_palavras,
        "total_letras": total_letra,
        "frequencia_palavras": frequencia_palavras,
        "palavra_mais_frequente": mais_frequente,
        "ocorrencias": ocorrencias
    }


txt = """Se eu moro em São Paulo, então eu moro no Brasil. Moro onde quiser"""
pprint(analisar_texto(txt))
