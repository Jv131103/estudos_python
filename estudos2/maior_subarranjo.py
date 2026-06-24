def maior_soma_subarranjo(nums, k):
    if len(nums) < k:
        return 0

    # 1. Calcula a soma da primeira janela
    janela_soma = sum(nums[:k])
    max_soma = janela_soma

    # 2. Desliza a janela pelo resto do array
    for i in range(k, len(nums)):
        # Adiciona o elemento que entra e remove o que sai
        janela_soma += nums[i] - nums[i - k]
        # Atualiza o máximo encontrado
        max_soma = max(max_soma, janela_soma)

    return max_soma


def maior_soma_subarranjo_na_mao(nums, k):
    if len(nums) < k:
        return 0

    # 1. Calcula a soma da primeira janela
    soma = 0
    for i in range(k):
        soma += nums[i]

    janela_soma = soma
    max_soma = janela_soma

    # 2. Desliza a janela pelo resto do array
    maior = max_soma if max_soma > janela_soma else janela_soma
    for i in range(k, len(nums)):
        # Adiciona o elemento que entra e remove o que sai
        janela_soma += nums[i] - nums[i - k]
        # Atualiza o máximo encontrado
        if max_soma > janela_soma:
            maior = max_soma
        else:
            maior = janela_soma
        max_soma = maior

    return max_soma


# Teste
print(maior_soma_subarranjo([2, 1, 5, 1, 3, 2], 3))  # Saída: 9 (subarranjo [5, 1, 3])
print(maior_soma_subarranjo_na_mao([2, 1, 5, 1, 3, 2], 3))  # Saída: 9 (subarranjo [5, 1, 3])
