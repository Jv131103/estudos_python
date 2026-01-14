"""
Faça um programa que leia um número n e mostre:

-n**2

(-n)**2
"""

n = int(input())

print(-n**2)  # Comportamento: -n * n = -resultado  (- com + == -), (+ com - == -)
print((-n)**2)  # Com,portamento: (-n) * (-n) = resultado (- com - == +), (+ com + == +)
