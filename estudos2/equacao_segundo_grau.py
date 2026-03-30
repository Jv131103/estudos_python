def delta(a, b, c):
    return b**2 - 4 * a * c


def calcular_equacao(a, b, c):
    if a == 0:
        return "não é uma equação do 2° grau"

    d = delta(a, b, c)
    if d < 0:
        return "não existem raízes reais"

    mais_x = (-b + d**(0.5)) / (2 * a)
    menos_x = (-b - d**(0.5)) / (2 * a)

    return mais_x, menos_x


print(calcular_equacao(1, -5, 6))
print(calcular_equacao(1, -4, 4))
print(calcular_equacao(0, -4, 4))
print(calcular_equacao(2, 2, 4))
