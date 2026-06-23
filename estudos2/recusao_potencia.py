def potencia(num, pot):
    if pot == 0:
        return 1

    return num * potencia(num, pot - 1)


def potencia2(num, pot):
    mult = 1
    for _ in range(pot):
        mult *= num

    return mult


print(potencia(2, 5))
print(potencia2(2, 5))
