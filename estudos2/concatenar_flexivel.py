def concatenar(*textos, separador=" "):
    textos = [str(texto) for texto in textos]
    return separador.join(textos)


print(concatenar("Python", "é", "legal"))
print(concatenar("a", "b", "c", separador="-"))
print(concatenar(1, True, "c", None, separador=" | "))
print(concatenar())
