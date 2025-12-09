def caracteres_unicos(string):
    string = string.lower().strip()

    dicionario_contador = {}

    for char in string:
        dicionario_contador[char] = dicionario_contador.get(char, 0) + 1

    for value in dicionario_contador.values():
        if value > 1:
            return False

    return True


print(caracteres_unicos("python"))
print(caracteres_unicos("banana"))
