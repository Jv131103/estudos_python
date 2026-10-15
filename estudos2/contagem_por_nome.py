def agrupar_por_inicial(lista):
    grupos = {}

    for nome in lista:
        grupos.setdefault(nome[0].lower(), []).append(nome)

    return grupos


def agrupar_por_inicial2(lista):
    grupos = {}

    for nome in lista:
        inicial = nome[0].lower()
        if inicial not in grupos:
            grupos[inicial] = [nome]
        else:
            grupos[inicial].append(nome)

    return grupos


print(agrupar_por_inicial(["Ana", "Arthur", "Bruno", "Beatriz", "Alice"]))
print(agrupar_por_inicial2(["Ana", "Arthur", "Bruno", "Beatriz", "Alice"]))
