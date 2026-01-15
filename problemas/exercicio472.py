"""
Faça um programa que:

Leia idade e se possui documento (True/False)

Use early return para verificar:

    se idade < 16 → "Entrada proibida"

    se idade ≥ 18 → "Entrada liberada"

    se idade entre 16 e 17:

    com documento → "Entrada liberada"

    sem documento → "Entrada proibida"

Evite aninhamento profundo.
"""


def pode_entrar(idade, possui_doc):
    if idade >= 18:
        return "Entrada Liberada"
    elif 16 <= idade <= 17:
        if possui_doc:
            return "Entrada Liberada"
    return "Entrada proibida"


print(pode_entrar(25, True))
print(pode_entrar(18, False))
print(pode_entrar(17, True))
print(pode_entrar(17, False))
print(pode_entrar(15, False))
