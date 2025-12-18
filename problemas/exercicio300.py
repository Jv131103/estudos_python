def contar_vogais(texto):
    vogais = "aeiou"
    total = 0
    for ch in texto.lower():
        if ch in vogais:
            total += 1
    return total


print(contar_vogais("Renato Justino"))
