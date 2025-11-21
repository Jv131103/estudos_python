def tamanho_string(texto):
    return len(texto)


def tamanho_string2(texto):
    tam = 0
    for _ in texto:
        tam += 1
    return tam


print(tamanho_string("olá mundo"))
print(tamanho_string2("olá mundo"))
