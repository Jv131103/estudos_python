def sacar_cedulas(valor):
    cedulas = [100, 50, 20, 10]
    usadas = []

    for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            usadas.extend([cedula] * quantidade)
            valor -= cedula * quantidade

    return usadas


print(sacar_cedulas(180))
print(sacar_cedulas(200))
print(sacar_cedulas(10))
print(sacar_cedulas(30))
print(sacar_cedulas(90))
print(sacar_cedulas(350))
print(sacar_cedulas(0))
print(sacar_cedulas(70))
