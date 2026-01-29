"""
Faça um programa que:

    Receba um texto contendo números de telefone no formato:

        (11) 98765-4321

    Use regex para:

        mascarar os 4 últimos dígitos

        manter o restante visível

    Resultado esperado:

        (11) 98765-****
"""


import re


def phone_is_valid(phone):
    return bool(re.match(r"^\(\d{2}\) \d{5}-\d{4}$", phone))


def sub_phone_number(phone):
    if not phone_is_valid(phone):
        return None
    return re.sub(r"\d{4}$", "****", phone)


def sub_phone_number_with_groups(phone):
    pattern = r"^(\(\d{2}\) \d{5}-)\d{4}$"
    return re.sub(pattern, r"\1****", phone)


print(sub_phone_number("(11) 98765-4321"))
print(sub_phone_number_with_groups("(11) 98765-4321"))
