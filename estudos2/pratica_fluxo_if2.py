vendas_mes = 3000

if vendas_mes < 3000:
    comissao = vendas_mes * 0.2
else:
    comissao = vendas_mes * 0.3

print(f"Comissão = R$ {comissao:.2f}")
