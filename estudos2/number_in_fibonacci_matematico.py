import math


def eh_quadrado_perfeito(x):
    s = int(math.isqrt(x))
    return s * s == x


def numero_em_fibonacci(n):
    if n < 0:
        return False
    return (
        eh_quadrado_perfeito(5 * n * n + 4)
        or eh_quadrado_perfeito(5 * n * n - 4)
    )


while True:
    try:
        num = int(input("Número: "))
        if numero_em_fibonacci(num):
            print("Ação bem-sucedida!")
        else:
            print("A ação falhou...")
        break
    except ValueError:
        print("Digite apenas números!")
