x1 = int(input("Forneça X (Um número entre 1 e 100000): "))
d1 = int(input("Forneça um número que X deverá ser divisível: "))

soma = 0

x1 += 1

while x1 > 0:
    x1 -= 1
    if x1 % d1 != 0:
        continue
    print(x1)
    soma += x1

print(f"Soma: {soma}")
