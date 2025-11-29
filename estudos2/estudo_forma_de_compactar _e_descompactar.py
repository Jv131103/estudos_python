import string


def compactar(texto):
    if not isinstance(texto, str):
        return "Tipo inválido"

    if not texto:
        return ""

    texto = texto.lower()
    d = {}

    for letra in texto:
        d[letra] = d.get(letra, 0) + 1

    compactado = ""
    for chave, valor in d.items():
        compactado += chave + str(valor)

    return compactado


def descompactar(texto_compactado):
    if not isinstance(texto_compactado, str):
        return "Tipo inválido"

    if not texto_compactado:
        return ""

    texto_compactado = texto_compactado.lower()
    descompactado = ""
    retorno = ""
    for valor in texto_compactado:
        if valor in string.ascii_lowercase:
            retorno = valor
        else:
            descompactado += str(retorno * int(valor))
    return descompactado


lista_a_compactar = [
    'aaabbc',
    'hhhhhh',
    'ab',
    'xxxyyyzz',
    '',
]

for valor in lista_a_compactar:
    retorno = compactar(valor)
    assert descompactar(retorno) == valor, f"Não passou em {valor}"
