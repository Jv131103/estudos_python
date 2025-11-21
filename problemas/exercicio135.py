numeros = range(1, 21)

quadrados_e_cubos = list(
    map(lambda i: (i, i**2 if i % 2 == 0 else i**3), numeros)
)

print(quadrados_e_cubos)
