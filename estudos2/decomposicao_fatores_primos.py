def is_prime(num):
    if num == 1:
        return False
    cont = 2
    while cont < num:
        if num % cont == 0:
            return False
        cont += 1
    return True


def decompor(n):
    valor_a_analisar = 2
    while n > 1:
        if is_prime(valor_a_analisar) and n % valor_a_analisar == 0:
            print(valor_a_analisar)
            n //= valor_a_analisar
            continue

        valor_a_analisar += 1


def decompor_otimizado(n):
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            print(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        print(n)


decompor(24)
print()
decompor_otimizado(24)
