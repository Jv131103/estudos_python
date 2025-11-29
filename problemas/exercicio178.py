def compactar(texto):
    if not isinstance(texto, str):
        return "Tipo inválido"

    if not texto:
        return ""

    resultado = []
    atual = texto[0]
    cont = 1

    for caractere in texto[1:]:
        if caractere == atual:
            cont += 1
        else:
            resultado.append(f"{atual}{cont}")
            atual = caractere
            cont = 1

    # não esquecer o último bloco
    resultado.append(f"{atual}{cont}")
    return "".join(resultado)


def descompactar(texto_compactado):
    if not isinstance(texto_compactado, str):
        return "Tipo inválido"

    if not texto_compactado:
        return ""

    resultado = []
    i = 0
    n = len(texto_compactado)

    while i < n:
        letra = texto_compactado[i]
        i += 1

        if i >= n or not texto_compactado[i].isdigit():
            return "Formato inválido"

        numeros = []
        while i < n and texto_compactado[i].isdigit():
            numeros.append(texto_compactado[i])
            i += 1

        quantidade = int("".join(numeros))
        resultado.append(letra * quantidade)

    return "".join(resultado)


lista_a_compactar = [
    'aaabbc',
    'hhhhhh',
    'ab',
    'xxxyyyzz',
    '',
    "ababa",
    "aaaaaaaaaaaa",
]

for valor in lista_a_compactar:
    retorno = compactar(valor)
    assert descompactar(retorno) == valor, f"Não passou em {valor}"
