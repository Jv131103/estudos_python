memo = {}


def fibmemo(n, chamadas=0):
    chamadas += 1
    if n in memo:
        return memo[n], chamadas

    if n <= 1:
        return n, chamadas

    res1, c1 = fibmemo(n - 1, chamadas)
    res2, c2 = fibmemo(n - 2, c1)

    memo[n] = res1 + res2
    return memo[n], c2


def fiblazy(n, chamadas=0):
    chamadas += 1
    if n <= 1:
        return n, chamadas

    res1, c1 = fiblazy(n - 1, chamadas)
    res2, c2 = fiblazy(n - 2, c1)

    return res1 + res2, c2


# Testando com N = 5
res_memo, qtd_memo = fibmemo(5)
res_lazy, qtd_lazy = fiblazy(5)

print(f"Fibmemo(5): Resultado = {res_memo} | Total de chamadas: {qtd_memo}")
print(f"Fiblazy(5): Resultado = {res_lazy} | Total de chamadas: {qtd_lazy}")
