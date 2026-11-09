def localizar_numero(numeros, alvo):
    resultado = {
        "primeiro": None,
        "ultimo": None,
        "ocorrencias": 0
    }

    for i, numero in enumerate(numeros):
        if numero == alvo:
            resultado["ocorrencias"] += 1
            if resultado["primeiro"] is None:
                resultado["primeiro"] = i

            resultado["ultimo"] = i

    return resultado


print(localizar_numero([4, 7, 4, 9, 4], 4))
print(localizar_numero([5, 2, 8], 5))
print(localizar_numero([9, 8, 7], 4))
print(localizar_numero([3, 3, 3], 3))
print(localizar_numero([2, 5, 2], 5))
print(localizar_numero([], 10))
