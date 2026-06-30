transacoes = [1500.00, -200.00, -50.50, 300.00, -12.00]  # Positivo = Depósito | Negativo = Saque

saldo_bancario = 0.0  # <-- ACUMULADORA

for movimentacao in transacoes:
    saldo_bancario += movimentacao  # O tamanho do incremento muda a cada linha

print(f"Saldo final consolidado: R$ {saldo_bancario:.2f}")
# Saída: Saldo final consolidado: R$ 1537.50
