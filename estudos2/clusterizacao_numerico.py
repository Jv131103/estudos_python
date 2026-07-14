numeros = [2, 3, 4, 18, 19, 20, 80, 82, 85]

numeros.sort()

clusters = [[numeros[0]]]

for numero in numeros[1:]:
    ultimo = clusters[-1][-1]

    if numero - ultimo <= 5:
        clusters[-1].append(numero)
    else:
        clusters.append([numero])

print(clusters)
