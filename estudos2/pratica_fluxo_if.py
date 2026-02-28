b = 100

if b != 50 * 2:
    b = b - 300
else:
    b = b + 300
    b = b + 1
    if b == 301:
        b = b + 2

print(f"Resposta: {b}")
