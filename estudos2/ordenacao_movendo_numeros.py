def mover_numeros(lista, numero, esquerda=False):
    trocou = False
    if not esquerda:
        slow = 0
        for fast in range(len(lista)):
            if lista[fast] != numero:
                if slow != fast:  # só conta como troca se mudou algo
                    trocou = True
                lista[slow], lista[fast] = lista[fast], lista[slow]
                slow += 1
    else:
        slow = len(lista) - 1
        for fast in range(len(lista) - 1, -1, -1):
            if lista[fast] != numero:
                if slow != fast:
                    trocou = True
                lista[slow], lista[fast] = lista[fast], lista[slow]
                slow -= 1
    return lista, trocou


arrays = [
    [10, 20, 12, 15, 0, 1, 8],
    [1, 2, 3, 4, 5, 6],
    [10, 9, 8, 7],
    [0, 1, 0, 3, 12]
]

for array in arrays:
    for i in range(len(array) // 2):
        trecho = array[i : len(array) - i]

        maior = max(trecho)
        menor = min(trecho)

        trecho, trocou_maior = mover_numeros(trecho, maior)
        trecho, trocou_menor = mover_numeros(trecho, menor, esquerda=True)

        array[i : len(array) - i] = trecho

        # print(f"passo {i + 1}: {array}")

        if not trocou_maior and not trocou_menor:
            # print("→ nenhuma troca, array já ordenado!")
            break

    print("final:", array)
