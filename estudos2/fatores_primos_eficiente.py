def fatores_primos(numero):
    fatores = []
    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero //= divisor
        else:
            divisor += 1

    if numero > 1:
        fatores.append(numero)

    return fatores


print(fatores_primos(60))
print(fatores_primos(84))
print(fatores_primos(13))
print(fatores_primos(100))
