def fatorial_linear(n):
    mult = 1
    for i in range(n, 0, -1):
        mult *= i
    return mult


def fatorial_recursivo(n):
    if n == 0:
        return 1
    return n * fatorial_recursivo(n - 1)


print(f"linear: {fatorial_linear(5)}")
print(f"recursivo: {fatorial_recursivo(5)}")
