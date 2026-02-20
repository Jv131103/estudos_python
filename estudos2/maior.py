maior = 0

for cont in range(1, 6):
    num = int(input(f"Numero {cont}: "))
    if num > maior:
        maior = num

print(maior)
