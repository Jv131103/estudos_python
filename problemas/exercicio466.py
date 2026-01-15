"""
Faça um programa que:

    Leia uma palavra

Mostre:

    os 3 primeiros caracteres (ou menos, se a palavra tiver < 3)

    os 3 últimos caracteres (ou menos)

    a palavra invertida sem usar [::-1] (use laço + concatenação ou lista + join)
"""


def function_tres_primeiros(palavra):
    tres_primeiros = ""

    limite = min(3, len(palavra))

    for indice in range(limite):
        tres_primeiros += palavra[indice]

    return tres_primeiros


def function_tres_ultimos(palavra):
    tres_ultimos = ""

    inicio = max(0, len(palavra) - 3)

    for i in range(inicio, len(palavra)):
        tres_ultimos += palavra[i]

    return tres_ultimos


def slicing(palavra, inicio, fim, intervalo):
    uniao = ""
    if inicio > fim:
        if intervalo > 0:
            intervalo = -intervalo

        for indice in range(inicio, fim, intervalo):
            uniao += palavra[indice]
    else:
        for indice in range(inicio, fim, abs(intervalo)):
            uniao += palavra[indice]

    return uniao


def inverter(palavra):
    resultado = ""
    for i in range(len(palavra) - 1, -1, -1):
        resultado += palavra[i]
    return resultado


palavra = input("Palavra: ").strip().lower()

tres_primeiros = function_tres_primeiros(palavra)
tres_ultimos = function_tres_ultimos(palavra)

invertido = slicing(palavra, len(palavra) - 1, -1, -1)

print(f"Três primeiros: {tres_primeiros}")
print(f"Três últimos: {tres_ultimos}")
print(f"Invertido: {invertido}")
