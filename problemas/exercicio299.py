def maior_palavra(frase):
    palavras = frase.split(" ")
    maior = ""
    for p in palavras:
        if len(p) > len(maior):
            maior = p
    return maior


def maior_palavra_elegante(frase):
    palavras = frase.split(" ")
    return max(palavras, key=lambda elemento: len(elemento))


print(maior_palavra("eu gosto muito de programar"))
print(maior_palavra_elegante("eu gosto muito de programar"))
