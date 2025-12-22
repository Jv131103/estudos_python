def contar_letras(texto):
    contador = {}
    for letra in texto:
        contador[letra] = contador.get(letra, 0) + 1
    return contador


def contar_letras_manual(texto):
    contador = {}
    for letra in texto:
        if letra not in contador:
            contador[letra] = 1
        else:
            contador[letra] += 1
    return contador


print(contar_letras("banana"))
print(contar_letras_manual("banana"))
