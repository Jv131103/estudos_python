def calc(limite):
    resultado = 0
    for numero in range(1, limite):
        resultado += numero
    return resultado


print(calc(10))
