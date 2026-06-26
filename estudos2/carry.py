def somar1_carry(lista):
    carry = 1  # Começamos com 1 porque queremos somar +1 ao número total

    for i in range(len(lista) - 1, -1, -1):
        soma = lista[i] + carry
        lista[i] = soma % 10   # Guarda o dígito atual (0 a 9)
        carry = soma // 10     # Calcula o "vai um" para a próxima rodada

    # Se ao final do loop o carry ainda for 1 (ex: [9,9,9] virou [0,0,0])
    if carry == 1:
        lista.insert(0, 1)     # Insere o 1 no início da lista

    print(lista)


somar1_carry([2, 9, 9])  # Resultado: [3, 0, 0]
somar1_carry([2, 3, 4])  # Resultado: [2, 3, 5] (Antes dava [3, 4, 5])
somar1_carry([9, 9, 9])  # Resultado: [1, 0, 0, 0]
