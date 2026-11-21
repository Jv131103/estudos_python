def editar_texto(comandos):
    novo = []
    for comando in comandos:
        if comando == "#":
            if novo:
                novo.pop()
        elif comando == "@":
            novo.clear()
        else:
            novo.append(comando)

    return "".join(novo)


print(editar_texto("abc##d"))
print(editar_texto("ab#c"))
print(editar_texto("a##b"))
print(editar_texto("abc@xy"))
print(editar_texto("ab@cd#e"))
print(editar_texto("####"))
print(editar_texto(""))
print(editar_texto("Python 3"))
print(editar_texto("@ab##xyz#"))
