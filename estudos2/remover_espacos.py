def remover_espacos(string):
    if not string:
        raise ValueError("STRING VAZIA!")

    dados = string.split()

    return " ".join(dados)


def remover_espacos_manual(string):
    string = string.strip()
    if not string:
        raise ValueError("STRING VAZIA!")

    uniao = ""

    i = 0

    for dados in string:
        if not dados.isspace():
            uniao += dados
            i = 0
        else:
            if i == 0:
                uniao += dados
                i += 1

    return uniao


def remover_espacos_manual2(string):
    string = string.strip()

    if not string:
        raise ValueError("STRING VAZIA!")

    uniao = ""

    qtd = 0
    for line in string:
        if line == " ":
            if not qtd:
                uniao += line
            qtd += 1
        else:
            uniao += line
            qtd = 0

    return uniao


print(remover_espacos("Python   é    muito   bom"))
print(remover_espacos_manual("Python   é    muito   bom"))
print(remover_espacos_manual2("Python   é    muito   bom"))
