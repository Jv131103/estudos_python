def soma_gauss(n):
    return n * (n + 1) // 2


def soma_intervalo_qualquer(a, b):
    termos = b - a + 1

    soma = termos * (a + b) // 2

    return soma


def soma_intervalo_loop(n):
    soma = 0

    while n > 0:
        soma += n
        n -= 1

    return soma


print(soma_gauss(5))
print(soma_intervalo_loop(5))
print(soma_intervalo_qualquer(1, 5))
