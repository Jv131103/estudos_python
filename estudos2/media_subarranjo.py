def media_subarranjo(nums, k):
    if len(nums) < k:
        return 0

    # 1. Calcula a soma da primeira janela
    janela_soma = sum(nums[:k])

    medias = []
    medias.append(janela_soma / k)
    # 2. Desliza a janela pelo resto do array
    for i in range(k, len(nums)):
        # Adiciona o elemento que entra e remove o que sai
        janela_soma += nums[i] - nums[i - k]
        # Pega a média
        medias.append(janela_soma / k)

    return medias


print(media_subarranjo([1, 3, 2, 6, -1, 4, 1, 8, 2], k=5))
