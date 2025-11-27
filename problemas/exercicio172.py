def contar_vogais(frase):
    frase = frase.lower()

    dicionario = {}

    total = 0

    for valor in frase:
        if valor in "aeiou":
            if valor not in dicionario:
                dicionario[valor] = 1
            else:
                dicionario[valor] += 1
            total += 1

    dicionario["total"] = total
    print(dicionario)


contar_vogais("Ola Mundo")
contar_vogais("Cachorro")
contar_vogais("arara")
contar_vogais("paralelepipedo")
contar_vogais("O rato roeu a roupa do rei de Roma")
