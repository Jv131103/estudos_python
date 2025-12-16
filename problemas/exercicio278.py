def comparar(a, b):
    if a == b:
        return "iguais"
    elif a < b:
        return f"{b} maior que {a}"
    else:
        return f"{a} maior que {b}"


print(comparar(2, 2))
print(comparar(3, 2))
print(comparar(2, 3))
