def compactar(string):

    if not string:
        return ""

    uniao = ""
    contador = 0

    valor_atual = string[0]
    for char in string:
        if char == valor_atual:
            contador += 1
        else:
            uniao += valor_atual + str(contador)
            contador = 1
            valor_atual = char

    uniao += valor_atual + str(contador)

    return uniao


print(compactar("aaabbccccdaa"))
print(compactar("aabbbccccbaa"))
print(compactar("aaaaaaaa"))
print(compactar(""))
print(compactar("   "))
