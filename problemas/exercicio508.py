"""
Faça um programa que:

    . Leia:

        . tipo_cliente ("vip" ou "normal")

        . forma_pagamento ("cartao" ou "dinheiro")

    . Use tabela de decisão para:

        . escolher a função de desconto correta

    . Cada função retorna o percentual de desconto

A tabela deve mapear estado → função.
"""


def desconto_vip_cartao():
    return 0.07


def desconto_vip_dinheiro():
    return 0.10


def desconto_normal_cartao():
    return 0.05


def desconto_normal_dinheiro():
    return 0.06


tabela = {
    ("vip", "cartao"): desconto_vip_cartao,
    ("vip", "dinheiro"): desconto_vip_dinheiro,
    ("normal", "cartao"): desconto_normal_cartao,
    ("normal", "dinheiro"): desconto_normal_dinheiro,
}

tipo_cliente = "vip"
forma_pagamento = "cartao"

funcao_desconto = tabela[(tipo_cliente, forma_pagamento)]
percentual = funcao_desconto()

print(f"Desconto: {percentual * 100:.0f}%")
