# CONTEXTO: Analisar o faturamento diário de uma loja na semana
faturamento_diario = [1200, 2500, 0, 3100, 850, 4000, 0]

# Inicialização dos papéis de variáveis
soma_total = 0          # ACUMULADORA (vai somar todo o dinheiro)
dias_com_venda = 0      # CONTADORA (vai contar quantos dias o faturamento foi > 0)
maior_venda = 0         # MELHOR CASO (vai caçar o recorde de vendas)
loja_falida = False     # ESTADO (se houver 3 ou mais dias zerados, ativa o alerta)
dias_zerados = 0        # CONTADORA AUXILIAR

# O loop alimenta a variável de iteração 'valor'
for valor in faturamento_diario:  # <-- 'valor' é ITERAÇÃO
    soma_total += valor          # Operador += alimentando ACUMULADORA

    if valor > 0:
        dias_com_venda += 1      # Operador += alimentando CONTADORA

        if valor > maior_venda:
            maior_venda = valor  # Redefinindo o MELHOR CASO
    else:
        dias_zerados += 1
        if dias_zerados >= 3:
            loja_falida = True   # Alterando a variável de ESTADO

# Computações finais com os dados refinados
media_faturamento = soma_total / dias_com_venda

print(f"Faturamento Total: R$ {soma_total}")
print(f"Média por dia útil: R$ {media_faturamento:.2f}")
print(f"Maior venda registrada: R$ {maior_venda}")
print(f"Alerta de falência ativo? {loja_falida}")
