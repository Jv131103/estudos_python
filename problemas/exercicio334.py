def comparar(texto):
    for i in range(len(texto)):
        for j in range(len(texto)):
            if i == j:
                print(texto[i], texto[j])


def comparar_limpo(texto):
    i = 0
    j = len(texto) - 1

    while i < j:
        print(texto[i], texto[j])
        i += 1
        j -= 1


comparar("arara")
print()
comparar_limpo("arara")
