def menor_janela(nums, alvo):
    left = 0
    soma = 0
    menor = float('inf')

    for right in range(len(nums)):
        soma += nums[right]

        while soma >= alvo:
            tamanho = right - left + 1
            menor = min(menor, tamanho)
            soma -= nums[left]
            left += 1

    return menor if menor != float('inf') else -1


print(menor_janela(nums=[2, 3, 1, 2, 4, 3], alvo=7))
