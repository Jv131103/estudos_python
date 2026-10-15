def somar_blocos(numeros):
    if not numeros:
        return []

    result = []
    soma = 0
    tem_bloco = False
    for numero in numeros:
        if numero == 0:
            if tem_bloco:
                result.append(soma)
            soma = 0
            tem_bloco = False
        else:
            soma += numero
            tem_bloco = True

    if tem_bloco:
        result.append(soma)

    return result


print(somar_blocos([10, 5, 0, 7, -2, 0, 4]))
print(somar_blocos([0, 3, 0, 0, 2]))
print(somar_blocos([5, 10, 15]))
print(somar_blocos([]))
