def normalizar_usuarios(lista):
    for valores in lista:
        valores["nome"] = valores["nome"].strip().capitalize()
        if valores["ativo"].upper() == "SIM":
            valores["ativo"] = True
        elif valores["ativo"].upper().replace("Ã", "A") == "NAO":
            valores["ativo"] = False
        else:
            print("Inválido, normalização não executada")
            return None

    return lista


usuarios = [
    {"nome": "  Ana  ", "ativo": "Sim"},
    {"nome": "Carlos", "ativo": "não"},
    {"nome": "  bruna ", "ativo": "SIM"},
]
print(normalizar_usuarios(usuarios))
