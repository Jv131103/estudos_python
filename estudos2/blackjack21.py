def calcular_pontos(cartas):
    soma = 0
    ases = 0

    for valor in cartas:
        valor = valor.upper().strip()
        if valor in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            soma += int(valor)
        elif valor in "JQK":
            soma += 10
        elif valor == "A":
            soma += 11
            ases += 1

    while soma > 21 and ases > 0:
        soma -= 10
        ases -= 1

    return soma


print(calcular_pontos(["A", "K"]))
print(calcular_pontos(["A", "A", "9"]))
print(calcular_pontos(["A", "9", "A", "5"]))
print(calcular_pontos(["K", "Q", "2"]))
print(calcular_pontos(["A", "A", "A", "9"]))
print(calcular_pontos(["5", "6", "10"]))
print(calcular_pontos([]))
print(calcular_pontos(["A", "A", "8"]))
print(calcular_pontos(["A", "9", "5"]))
print(calcular_pontos(["A", "A", "K", "K", "K"]))
print(calcular_pontos(["A", "K", "5"]))
print(calcular_pontos(["A", "A", "A", "9"]))
print(calcular_pontos(["A", "A", "A", "K", "K", "K"]))
