def comprimir(string):
    if not isinstance(string, str):
        raise TypeError("String precisa ser do tipo STR")

    if not string:
        raise ValueError("String não pode ser vazia")

    cont = 1

    anterior = string[0]
    comprimido = []

    for i in range(1, len(string)):
        if string[i] == anterior:
            cont += 1
        else:
            comprimido.extend([anterior, str(cont)])
            cont = 1
            anterior = string[i]

    comprimido.extend([anterior, str(cont)])
    return "".join(comprimido) if len(comprimido) < len(string) else string


print(comprimir("aaabbccccdd"))
print(comprimir("abcd"))
