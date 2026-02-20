num = int(input("Numero 1: "))

menor = num

for cont in range(1, 5):
    num = int(input(f"Numero {cont + 1}: "))
    if num < menor:
        menor = num

print(menor)
