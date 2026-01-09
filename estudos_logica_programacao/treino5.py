n1 = int(input())
n2 = int(input())

if n1 > n2:
    temp = n2
    n2 = n1
    n1 = temp

total = 0

while n1 <= n2:
    n1 *= 1.01
    total += 1

print(f"Valor obtido: {n1}")
print(f"Total de iterações: {total}")
