def inverter_string(string):
    indice_final = len(string) - 1

    inverso = ""
    for i in range(indice_final, -1, -1):
        inverso += string[i]

    return inverso


def inverter_string_recursivo(string, indice_final):
    if indice_final < 0:
        return ""
    return string[indice_final] + inverter_string_recursivo(string, indice_final - 1)


print(inverter_string("python"))
print(inverter_string_recursivo("python", len("python") - 1))
