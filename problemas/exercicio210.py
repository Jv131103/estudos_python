def soma_digitos_recursivo(n):
    if n <= 0:
        return 0

    return n % 10 + soma_digitos_recursivo(n // 10)


print(soma_digitos_recursivo(1234))
