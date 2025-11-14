def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def numeros_primos_de(inicio, fim):
    while inicio < fim:
        if is_prime(inicio):
            print(inicio, end=" ")
        inicio += 1
    print()


numeros_primos_de(1, 100)
