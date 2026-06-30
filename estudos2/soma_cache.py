cache = {}


def soma(n1, n2):
    # Criamos uma chave padronizada (sempre do menor para o maior)
    chave = (min(n1, n2), max(n1, n2))

    if cache.get(chave):
        print("cache")
        return cache[chave]

    print("no cache")
    resultado = n1 + n2
    cache[chave] = resultado
    return resultado


print(soma(3, 3))
print(soma(3, 3))
print(soma(3, 2))
print(soma(3, 2))
print(soma(2, 3))
