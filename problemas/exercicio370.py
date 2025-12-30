def maior_substring_consecutiva(texto):
    if not texto:
        return ""

    atual = texto[0]
    maior = atual

    for i in range(1, len(texto)):
        if ord(texto[i]) == ord(texto[i - 1]) + 1:
            atual += texto[i]
        else:
            atual = texto[i]

        if len(atual) > len(maior):
            maior = atual

    return maior


print(maior_substring_consecutiva("abcmnopzab"))
