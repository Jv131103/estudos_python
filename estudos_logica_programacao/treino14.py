x = int(input("Forneça X (1 a 100000): "))
d1 = int(input("Divisor principal (d1): "))
d2 = int(input("Divisor de bloqueio (d2): "))

soma = 0

x += 1

while x > 0:
    x -= 1

    if x % d1 != 0:
        continue

    if x % d2 == 0:
        print(f"Valor que causou obstrução: {x}")
        break

    print(x)
    soma += x
else:
    print("Não houve obstrução no laço. A soma está completa.")

print(f"Soma: {soma}")
