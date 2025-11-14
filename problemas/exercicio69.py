def fibonacci_ate(a):
    if a < 0:
        return 0

    n1 = 0
    n2 = 1
    contador = 0
    print(n1, n2, end=" ")
    while contador < a:
        n1, n2 = n2, n1 + n2
        print(n2, end=" ")
        contador += 1
    print()


fibonacci_ate(10)
