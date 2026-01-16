"""
Crie uma função potencia(base, expoente=2) que calcule a potência de um número,
usando valor padrão para o expoente.
"""


def potencia(base, expoente=2):
    if not isinstance(base, (int, float)):
        print("Base precisa ser do tipo numérico")
        return

    if not isinstance(expoente, (int, float)):
        print("Expoente precisa ser do tipo numérico")
        return

    return base**expoente


print(potencia(2))
print(potencia(2, 3))
print(potencia(2, 4))
