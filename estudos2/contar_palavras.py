def contar(texto):
    texto = texto.strip().lower()

    novo = ""
    for char in texto:
        if char in "?!@#$%¨&*/:.,^~´`'=+-_\\|":
            continue

        novo += char

    d = {}

    frases = novo.split()

    for frase in frases:
        d[frase] = d.get(frase, 0) + 1

    return d


print(contar("O gato viu o rato. O rato fugiu!"))
