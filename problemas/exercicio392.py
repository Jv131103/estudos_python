def contar_letras(texto):
    texto = texto.lower()

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
    vogais = 'aeiou'
    d = {
        "vogais": 0,
        "consoantes": 0
    }
    for chars in texto:
        if chars in vogais:
            d["vogais"] += 1
        elif chars.isalpha():
            d["consoantes"] += 1

    return d


print(contar_letras("Ola Mundo 2026"))
