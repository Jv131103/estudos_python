def processar_pedido(estado_inicial, acoes):
    estado_atual = estado_inicial
    recusas = 0

    for acao in acoes:
        if estado_atual == "criado" and acao == "pagar":
            estado_atual = "pago"
        elif estado_atual == "pago" and acao == "enviar":
            estado_atual = "enviado"
        elif estado_atual == "enviado" and acao == "entregar":
            estado_atual = "entregue"
        elif estado_atual in ["criado", "pago"] and acao == "cancelar":
            estado_atual = "cancelado"
        else:
            recusas += 1

    return estado_atual, recusas


def processar_pedido2(estado_inicial, acoes):
    estado_atual = estado_inicial
    recusas = 0

    tabela = {
        ("criado", "pagar"): "pago",
        ("pago", "enviar"): "enviado",
        ("enviado", "entregar"): "entregue",
        ("criado", "cancelar"): "cancelado",
        ("criado, pago"): "cancelado",
    }

    for acao in acoes:
        chave = (estado_atual, acao)

        if chave in tabela:
            estado_atual = tabela[chave]
        else:
            recusas += 1

    return estado_atual, recusas


print(processar_pedido(
    "criado", ["pagar", "enviar", "entregar"]
))
print(processar_pedido(
    "criado", ["entregar", "pagar", "enviar"]
))
print(processar_pedido(
    "criado", ["cancelar", "pagar"]
))
print(processar_pedido(
    "pago", ["cancelar"]
))
print(processar_pedido(
    "enviado", ["cancelar", "entregar"]
))
print(processar_pedido(
    "criado", []
))
print()
print(processar_pedido2(
    "criado", ["pagar", "enviar", "entregar"]
))
print(processar_pedido2(
    "criado", ["entregar", "pagar", "enviar"]
))
print(processar_pedido2(
    "criado", ["cancelar", "pagar"]
))
print(processar_pedido2(
    "pago", ["cancelar"]
))
print(processar_pedido2(
    "enviado", ["cancelar", "entregar"]
))
print(processar_pedido2(
    "criado", []
))
