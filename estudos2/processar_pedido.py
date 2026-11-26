def processar_pedido(estado_inicial, acoes):
    estado_atual = estado_inicial
    historico = [estado_atual]
    recusas = 0

    for acao in acoes:
        if estado_atual == "criado" and acao == "pagar":
            estado_atual = "pago"
            historico.append(estado_atual)
        elif estado_atual == "pago" and acao == "enviar":
            estado_atual = "enviado"
            historico.append(estado_atual)
        elif estado_atual == "enviado" and acao == "entregar":
            estado_atual = "entregue"
            historico.append(estado_atual)
        elif estado_atual in ["criado", "pago"] and acao == "cancelar":
            estado_atual = "cancelado"
            historico.append(estado_atual)
        else:
            recusas += 1

    return estado_atual, recusas, historico


def processar_pedido2(estado_inicial, acoes):
    estado_atual = estado_inicial
    recusas = 0
    historico = [estado_atual]

    tabela = {
        ("criado", "pagar"): "pago",
        ("pago", "enviar"): "enviado",
        ("enviado", "entregar"): "entregue",
        ("criado", "cancelar"): "cancelado",
        ("pago", "cancelar"): "cancelado",
    }

    for acao in acoes:
        chave = (estado_atual, acao)

        if chave in tabela:
            estado_atual = tabela[chave]
            historico.append(estado_atual)
        else:
            recusas += 1

    return estado_atual, recusas, historico


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
print(processar_pedido("pago", ["cancelar"]))
print(processar_pedido(
    "enviado", ["cancelar", "entregar"]
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
print(processar_pedido2("pago", ["cancelar"]))
print(processar_pedido2(
    "enviado", ["cancelar", "entregar"]
))
