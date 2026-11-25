def controlar_estoque(estoque_inicial, movimentos):
    retiradas_recusadas = 0

    for valor in movimentos:
        if estoque_inicial + valor < 0:
            retiradas_recusadas += 1
        else:
            estoque_inicial += valor

    return estoque_inicial, retiradas_recusadas


print(controlar_estoque(5, [3, -4, -10, 2, -3]))
print(controlar_estoque(0, [-1, 2, -2]))
print(controlar_estoque(10, []))
print(controlar_estoque(2, [-2, -1, 5]))
print(controlar_estoque(4, [0, -4, 3]))
