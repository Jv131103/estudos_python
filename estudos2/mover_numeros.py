def mover_numeros(lista, numero, esquerda=False):
    if not esquerda:
        slow = 0
        for fast in range(len(lista)):
            if lista[fast] != numero:
                lista[slow], lista[fast] = lista[fast], lista[slow]
                slow += 1
    else:
        slow = len(lista) - 1
        for fast in range(len(lista) - 1, -1, -1):
            if lista[fast] != numero:
                lista[slow], lista[fast] = lista[fast], lista[slow]
                slow -= 1
    return lista


array = [10, 20, 12, 15, 0, 1, 8]

for i in range(len(array) // 2):
    # fatia ainda não ordenada
    trecho = array[i : len(array) - i]

    maior = max(trecho)
    menor = min(trecho)

    # opera só no trecho relevante
    mover_numeros(trecho, maior)             # maior vai para a direita do trecho
    mover_numeros(trecho, menor, esquerda=True)  # menor vai para a esquerda do trecho

    # escreve o trecho de volta (slices são cópias em Python)
    array[i : len(array) - i] = trecho

    print(f"passo {i + 1}: {array}")

print("final:", array)
