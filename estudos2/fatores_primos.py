def fatores_primos(numero):
    divisor = 2
    fatores = []
    while numero > 1:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero //= divisor
        else:
            divisor += 1

    return fatores


print(fatores_primos(60))
print(fatores_primos(84))
print(fatores_primos(13))
print(fatores_primos(100))
