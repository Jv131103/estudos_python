def simular_troco(valor_compra, valor_pago):
    compra = int(round(valor_compra * 100))  # Usa com centavos
    pago = int(round(valor_pago * 100))

    if pago < compra:
        return f"Falta R$ {(compra - pago) / 100:.2f}"
    elif pago > compra:
        return f"Troco: R$ {(pago - compra) / 100:.2f}"
    else:
        return "Sem troco"


print(simular_troco(37.50, 50))
print(simular_troco(150, 50))
print(simular_troco(50, 50))
