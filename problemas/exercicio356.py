def media_positivos(numeros):
    if not numeros:
        return None

    soma = 0
    cont = 0

    for n in numeros:
        if n > 0:
            soma += n
            cont += 1

    if not cont:
        return None

    return soma / cont


print(media_positivos([10, -5, 20, 0, 5]))
print(media_positivos([-1, -2, -3]))
print(media_positivos([]))
