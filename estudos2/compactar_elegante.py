def compactar(s: str) -> str:
    if not s:
        return ""

    partes = []
    atual = s[0]
    cont = 0

    for ch in s:
        if ch == atual:
            cont += 1
        else:
            partes.append(atual)
            partes.append(str(cont))
            atual = ch
            cont = 1

    partes.append(atual)
    partes.append(str(cont))

    return "".join(partes)


print(compactar("aaabbccccdaa"))
print(compactar("aabbbccccbaa"))
print(compactar("aaaaaaaa"))
print(compactar(""))
print(compactar("   "))
