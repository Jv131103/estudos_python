cache = {}


def quadrado(x):
    if x in cache:
        print("Usando cache")
        return cache[x]

    print("Sem cache")
    resultado = x * x

    cache[x] = resultado

    return resultado


print(quadrado(5))
print(quadrado(5))
print(quadrado(6))
print(quadrado(9))
print(quadrado(9))
