def analisar_texto(texto):
    resultado = {
        "vogais": 0,
        "consoantes": 0,
        "outros": 0
    }

    for caractere in texto.lower():
        caractere = caractere

        if caractere in "aeiou":
            resultado["vogais"] += 1

        elif caractere in "bcdfghjklmnpqrstvwxyz":
            resultado["consoantes"] += 1

        else:
            resultado["outros"] += 1

    return resultado


print(analisar_texto("Casa"))
print(analisar_texto("AEIOU"))
print(analisar_texto("Python 3.13!"))
print(analisar_texto("aB!"))
print(analisar_texto("123_?"))
print(analisar_texto(""))
