def normalizar_usuarios(lista):
    for user in lista:
        # Normaliza o nome
        user["nome"] = user["nome"].strip().title()

        # Normaliza o campo ativo
        ativo = user["ativo"].strip().upper()

        if ativo in ("SIM", "S"):
            user["ativo"] = True
        elif ativo in ("NAO", "N", "NÃO"):
            user["ativo"] = False
        else:
            print(f"Valor inválido para 'ativo': {user['ativo']}")
            return None

    return lista


usuarios = [
    {"nome": "  Ana  ", "ativo": "Sim"},
    {"nome": "Carlos", "ativo": "não"},
    {"nome": "  bruna ", "ativo": "SIM"},
]
print(normalizar_usuarios(usuarios))
