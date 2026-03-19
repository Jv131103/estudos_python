def modelo1(frase):
    frase = frase.lower().split()
    if not frase:
        return

    dados = {}

    for texto in frase:
        dados[texto] = dados.get(texto, 0) + 1

    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


def modelo2(frase):
    frase = frase.lower().split()
    if not frase:
        return

    dados = {}

    for texto in frase:
        if texto in dados:
            dados[texto] += 1
        else:
            dados[texto] = 1

    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


def modelo3(frase):
    frase = frase.lower().split()
    if not frase:
        return

    ja_foi = []

    for texto in frase:
        cont = 0
        if texto not in ja_foi:
            for validar in frase:
                if validar == texto:
                    cont += 1
            print(f"{texto}: {cont}")
            ja_foi.append(texto)


def modelo4(frase):
    frase = frase.lower().split()
    if not frase:
        return

    ja_foi = []

    for texto in frase:
        if texto not in ja_foi:
            print(f"{texto}: {frase.count(texto)}")
            ja_foi.append(texto)


def modelo5(frase):
    palavras = frase.lower().split()
    if not palavras:
        return
    dados = dict.fromkeys(palavras, 0)
    for texto in palavras:
        dados[texto] += 1
    for chave, valor in sorted(dados.items()):
        print(f"{chave}: {valor}")


def modelo6(frase):
    palavras = sorted(frase.lower().split())
    if not palavras:
        return

    anterior = palavras[0]
    cont = 1
    dados = []
    for i in range(1, len(palavras)):
        if palavras[i] == anterior:
            cont += 1
        else:
            dados.append([anterior, cont])
            cont = 1
            anterior = palavras[i]

    dados.append([anterior, cont])

    for dado in dados:
        palavra, total = dado
        print(f"{palavra}: {total}")


if __name__ == "__main__":
    modelo1("o gato viu o rato e o rato fugiu")
    print()
    modelo2("o gato viu o rato e o rato fugiu")
    print()
    modelo3("o gato viu o rato e o rato fugiu")
    print()
    modelo4("o gato viu o rato e o rato fugiu")
    print()
    modelo5("o gato viu o rato e o rato fugiu")
    print()
    modelo6("o gato viu o rato e o rato fugiu")
