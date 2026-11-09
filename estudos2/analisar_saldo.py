def analisar_saldo(movimentacoes, saldo_inicial):
    maior_saldo = saldo_inicial
    saldo_final = saldo_inicial
    vezes_negativo = 0
    recuperacoes = 0
    primeiro_negativo = None
    historico = []

    for idx, valor in enumerate(movimentacoes):
        saldo_anterior = saldo_final
        saldo_final += valor
        if saldo_final > maior_saldo:
            maior_saldo = saldo_final
        if saldo_final < 0:
            vezes_negativo += 1
            if primeiro_negativo is None:
                primeiro_negativo = idx
        if saldo_anterior < 0 and saldo_final >= 0:
            recuperacoes += 1

        historico.append(saldo_final)

    return {
        "saldo_final": saldo_final,
        "maior_saldo": maior_saldo,
        "vezes_negativo": vezes_negativo,
        "primeiro_negativo": primeiro_negativo,
        "recuperacoes": recuperacoes,
        "historico": historico
    }


print(analisar_saldo([10, -5, -30, 12, -4], 20))
print(analisar_saldo([-10, -5, 20, -8], 5))
print(analisar_saldo([-5, -10], 20))
print(analisar_saldo([-20, 2, 3, 20, 1], 10))
print(analisar_saldo([15], -10))
