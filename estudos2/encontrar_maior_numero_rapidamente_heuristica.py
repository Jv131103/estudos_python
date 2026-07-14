import random

numeros = [random.randint(1, 10000) for _ in range(1000000)]

# Heurística: olhar apenas os primeiros 100 números
maior = max(numeros[:100])

print(maior)
