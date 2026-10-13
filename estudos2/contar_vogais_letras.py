def contar_vogais(letra):
    if not isinstance(letra, str):
        raise TypeError("Formato inválido de 'letra'")

    cont = 0
    for valor in letra.lower():
        if valor in "aeiou":
            cont += 1

    return cont


print(contar_vogais("Renato"))
print(contar_vogais("PYTHON"))
print(contar_vogais("xyz"))
print(contar_vogais("ola mundo"))
