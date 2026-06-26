def razao(lista, qtd_slow=1, qtd_fast=2):
    """
    Percorre a lista com dois ponteiros (slow e fast) e retorna o elemento
    onde slow para quando fast chega ao final.

    A posição final de slow é aproximadamente:
        slow_final ≈ (qtd_slow / qtd_fast) * len(lista)

    Porém, quando fast não divide o tamanho da lista exatamente,
    ele ultrapassa o fim — e slow para antes do esperado pela razão.

    Testes com list(range(10)):
        razao(lista, 1, 4) → slow=3  (1/4 de 10 ≈ 2.5, arredonda para 3)
        razao(lista, 2, 5) → slow=4  (2/5 de 10 = 4.0, exato)
        razao(lista, 3, 7) → slow=6  (3/7 de 10 ≈ 4.3, mas fast ultrapassa
                                       o fim em 1 iteração extra → slow=6)

    Parâmetros:
        lista     : lista de elementos
        qtd_slow  : quanto slow avança por iteração (padrão: 1)
        qtd_fast  : quanto fast avança por iteração (padrão: 2)

    Retorna:
        O elemento em lista[slow] quando fast >= len(lista)
    """
    slow = 0
    fast = 0
    while fast < len(lista):
        slow += qtd_slow
        fast += qtd_fast
    return lista[slow]


print(razao(list(range(10)), 1, 4))
print(razao(list(range(10)), 2, 5))
print(razao(list(range(10)), 3, 7))
