def inverter(texto):
    resultado = ""
    for i in range(len(texto) - 1, -1, -1):
        resultado += texto[i]
    return resultado


def inverter_elegante(texto):
    return "".join([texto[i] for i in range(len(texto) - 1, -1, -1)])


def inverter_pythonico(texto):
    return texto[::-1]


print(inverter("python"))
print(inverter_elegante("python"))
print(inverter_pythonico("python"))
