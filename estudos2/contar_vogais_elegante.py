def contar_vogais(frase):
    frase = frase.lower()
    d = {}

    for letra in frase:
        if letra in "aeiou":
            d[letra] = d.get(letra, 0) + 1

    d["total"] = sum(d.values())
    print(d)


contar_vogais("Ola Mundo")
contar_vogais("Cachorro")
contar_vogais("arara")
contar_vogais("paralelepipedo")
contar_vogais("O rato roeu a roupa do rei de Roma")
