def maior_volume(lista):
    i = 0
    j = len(lista) - 1

    area_maxima = 0

    while i < j:
        largura = j - i
        altura_minima = min(lista[i], lista[j])
        area_atual = largura * altura_minima
        area_maxima = max(area_maxima, area_atual)
        if lista[i] < lista[j]:
            i += 1
        else:
            j -= 1

    return area_maxima


print(maior_volume([1, 8, 6, 2, 5, 4, 8, 3, 7]))
