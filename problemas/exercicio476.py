"""
Leia um valor qualquer.

    Se for None → imprima "Sem valor"

    Se for string vazia ou só espaços → "Texto vazio"

    Se for número:

        maior que zero → "Positivo"

        menor que zero → "Negativo"

        zero → "Zero"

Dica: combine is, strip(), isinstance(), operadores relacionais.
"""


def value_is(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    return "Zero"


def verificar(valor):
    if valor is None:
        return "Sem valor"

    if isinstance(valor, str):
        if not valor or not valor.strip():
            return "Texto vazio"
        return "Valor textual"

    if isinstance(valor, (int, float)):
        return value_is(valor)

    return "Tipo desconhecido"


print(verificar("Ola"))
print(verificar(None))
print(verificar(""))
print(verificar(" "))
print(verificar("    "))
print(verificar(1))
print(verificar(0))
print(verificar(-1))
print(verificar(1.2))
print(verificar(-1.2))
