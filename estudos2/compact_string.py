def compactar_string(string):
    if not string:
        return ""

    cont = 0
    anterior = string[0]
    dados = []
    for char in string:
        if char == anterior:
            cont += 1
        else:
            dados.append(f"{anterior}{cont}")
            cont = 1
            anterior = char

    dados.append(f"{anterior}{cont}")

    return "".join(dados)


print(compactar_string("aaabbc"))
print(compactar_string("abcd"))
print(compactar_string("aaaa"))
print(compactar_string("aabbaa"))
print(compactar_string(""))
