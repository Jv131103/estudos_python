def validar_resultado(a, b, c, d):
    if not d:
        print("O parâmetro d não pode ser 0")
        return

    r = d + (a - b * c) / d

    if r > 0:
        print("Resultado positivo")
    elif r < 0:
        print("Resultado negativo")

    return r


a = float(input())
b = float(input())
c = float(input())
d = float(input())

r = validar_resultado(a, b, c, d)
print(r)
