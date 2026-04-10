# Sem cache
def lento(n):
    print("Calculando...")
    return n * n


print(lento(5))
print(lento(5))  # recalcula de novo

print()

# Com cache
cache = {}


def rapido(n):
    if n in cache:
        print("Pegou do cache!")
        return cache[n]

    print("Calculando...")
    resultado = n * n
    cache[n] = resultado
    return resultado


print(rapido(5))
print(rapido(5))  # agora é rápido
