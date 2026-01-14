"""
Faça um programa que:

    Leia dois valores decimais

    Some os dois

    Compare o resultado com um terceiro valor

    Use abs() para lidar com erro de precisão
"""


def float_igual(a, b, rel_tol=1e-9, abs_tol=1e-12):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


n1 = float(input().replace(",", "."))
n2 = float(input().replace(",", "."))

soma = n1 + n2

terceiro_valor = 1.2

print(soma == terceiro_valor)

precisao_melhorada = float_igual(soma, terceiro_valor)

print(precisao_melhorada)
