def processar_eventos(eventos):
    ligado = False

    soma = 0
    qtd = 0
    processados = []
    ignorados = []

    resultado = {}

    for evento in eventos:
        if evento == "LIGAR":
            ligado = True
        elif evento == "DESLIGAR":
            ligado = False
        elif ligado and isinstance(evento, (int, float)):
            soma += evento
            processados.append(evento)
            qtd += 1
        else:
            ignorados.append(evento)

    resultado["soma"] = soma
    resultado["quantidade"] = qtd
    resultado["processados"] = processados
    resultado['ignorados'] = ignorados

    return resultado


print(processar_eventos(["LIGAR", 5, 3, "DESLIGAR", 10, "LIGAR", -2, 4]))
print(processar_eventos([2, 5, "LIGAR", 8, "DESLIGAR", 3]))
print(processar_eventos([]))
