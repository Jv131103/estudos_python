"""
Crie uma função contar_vogais(texto) que retorne a quantidade de vogais
presentes em uma string.
"""


def contar_vogais(texto):
    texto = texto.strip().lower()

    mapa = {
        "á": "a", "à": "a", "ã": "a", "â": "a",
        "é": "e", "ê": "e",
        "í": "i",
        "ó": "o", "ô": "o", "õ": "o",
        "ú": "u",
        "ç": "c",
    }
    resultado = ""
    for c in texto:
        if c in mapa:
            resultado += mapa[c]
        else:
            resultado += c

    texto = resultado
    vogais = "aeiou"

    dicionario = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for char in texto:
        if char in vogais:
            dicionario[char] = dicionario.get(char, 0) + 1

    return dicionario


def contar_vogais_apenas_total(texto):
    texto = texto.lower()

    mapa = {
        "á": "a", "à": "a", "ã": "a", "â": "a",
        "é": "e", "ê": "e",
        "í": "i",
        "ó": "o", "ô": "o", "õ": "o",
        "ú": "u",
    }

    vogais = "aeiou"
    total = 0

    for c in texto:
        c = mapa.get(c, c)
        if c in vogais:  # type: ignore
            total += 1

    return total


print(contar_vogais("Ola"))
print(contar_vogais("Batata Doce"))
print(contar_vogais("Rosas são vermelhas e violetas são azuis"))
print(contar_vogais("O rato roeu a roupa do rei de Roma"))
print()
print(contar_vogais_apenas_total("Ola"))
print(contar_vogais_apenas_total("Batata Doce"))
print(contar_vogais_apenas_total("Rosas são vermelhas e violetas são azuis"))
print(contar_vogais_apenas_total("O rato roeu a roupa do rei de Roma"))
