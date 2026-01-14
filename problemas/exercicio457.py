"""
Faça um programa que:

    Leia dois valores com input()

Mostre:

    o tipo original

    tente somar sem casting (observe o erro)

    depois faça o casting correto e some

Use comentários para explicar o comportamento.
"""

val1 = input()  # Lê texto puro
val2 = input()  # Lê texto puro

# Ideal: Apenas números para que o segundo caso rode sem tratamento
soma_sem_casting = val1 + val2  # Sem casting, haverá concatenação
soma_com_casting = int(val1) + int(val2)  # Com casting, realizará a soma, mas pode dar erros em casos de ponto flutuante, ou textos puros

print(soma_sem_casting)
print(soma_com_casting)
