ladoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))
ladoC = float(input('Lado C: '))

if ladoA == ladoB == ladoC:
    print('O triângulo é equilátero.')
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')
