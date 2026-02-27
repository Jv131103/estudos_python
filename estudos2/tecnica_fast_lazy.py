lista = list(range(10))

lazy = 0

for fast in range(2, len(lista)):
    print(lista[lazy], lista[fast])
    lazy += 1
