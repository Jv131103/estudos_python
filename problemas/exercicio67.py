"""
Considere um número inteiro positivo n especificado pelo usuário.

Elabore um programa que calcule e mostre na tela:

    A soma dos n primeiros números inteiros não-nulos (1+2+3+ ... +n) ;

    A soma dos n primeiros números pares;

    A soma dos n primeiros números ímpares.
"""


def retornar_somas(n):
    soma_ate_n = 0
    soma_pares_ate_n = 0
    soma_impares_ate_n = 0
    for i in range(n):
        if i % 2 == 0:
            soma_pares_ate_n += i
        else:
            soma_impares_ate_n += i
        soma_ate_n += i
    return soma_ate_n, soma_pares_ate_n, soma_impares_ate_n


soma_total, soma_pares, soma_impares = retornar_somas(10)
print(soma_total)
print(soma_pares)
print(soma_impares)
