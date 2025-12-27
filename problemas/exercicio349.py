def maior(num1, num2):
    return num1 if num1 > num2 else num2


valores = [
    (1, 2),
    (2, 1),
    (2, 2),
]

for itens in valores:
    n1, n2 = itens
    print(maior(n1, n2))
