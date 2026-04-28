import numpy as np

# Operações algébricas entre arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Adição
c = a + b
print(f"soma dos vetores: {c}")
print()

# Subtração
d = a - b
print(f"subtração dos vetores: {d}")
print()

# Multiplicação
e = a * b
print(f"multiplicação dos vetores: {e}")
print()

# Divisão
f = a / b
print(f"Divisão real dos vetores: {f}")
print()

print(c, d, e, f)
# Saída: [5 7 9] [-3 -3 -3] [4 10 18] [0.25 0.4 0.5]
