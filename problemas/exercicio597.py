"""
Faça um programa que:

    Tenha uma função que simule algo “caro” (ex.: cálculo ou print)

    Use essa função dentro de um if

    Garanta que a função seja chamada apenas uma vez

    Use walrus para guardar o resultado
"""


def funcao_cara():
    print("CALCULANDO...")
    return 42


# Sem Walrus
resultado = funcao_cara()
if resultado > 10:
    print(resultado)


# Walrus
if (resultado := funcao_cara()) > 10:
    print(resultado)
