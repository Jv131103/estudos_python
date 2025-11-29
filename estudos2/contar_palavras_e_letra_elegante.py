import string
from collections import Counter
from pprint import pprint


def analisar_texto(texto):
    texto = texto.lower()

    # remove pontuações
    texto = texto.translate(str.maketrans("", "", string.punctuation))

    palavras = texto.split()

    total_palavras = len(palavras)
    total_letras = sum(len(p) for p in palavras)

    contagem = Counter(palavras)
    mais_frequente, ocorrencias = contagem.most_common(1)[0]

    return {
        "total_palavras": total_palavras,
        "total_letras": total_letras,
        "frequencia_palavras": dict(contagem),
        "palavra_mais_frequente": mais_frequente,
        "ocorrencias": ocorrencias
    }


txt = """Se eu moro em São Paulo, então eu moro no Brasil. Moro onde quiser"""
pprint(analisar_texto(txt))
