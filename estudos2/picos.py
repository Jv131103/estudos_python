def detectar_picos(lista):
    picos = []
    n = len(lista)

    # Se a lista tiver menos de 2 elementos, não há como definir um pico comparativo
    if n < 2:
        return picos

    for i in range(n):
        # Verifica a borda esquerda (primeiro elemento)
        if i == 0:
            if lista[i] > lista[i + 1]:
                picos.append(i)
        # Verifica a borda direita (último elemento)
        elif i == n - 1:
            if lista[i] > lista[i - 1]:
                picos.append(i)
        # Verifica os elementos do meio
        else:
            if lista[i] > lista[i - 1] and lista[i] > lista[i + 1]:
                picos.append(i)

    return picos


if __name__ == "__main__":
    # Teste 1 (Picos nos índices 1, 3, 5 -> valores 5, 7, 8)
    lista1 = [1, 5, 2, 7, 3, 8, 1]
    print(f"Lista 1: {detectar_picos(lista1)}")  # Saída: [1, 3, 5]

    # Teste 2 (Lista muito curta)
    lista2 = [1]
    print(f"Lista 2: {detectar_picos(lista2)}")  # Saída: []

    # Teste 3 (Pico na borda -> índice 1, valor 2)
    lista3 = [1, 2]
    print(f"Lista 3: {detectar_picos(lista3)}")  # Saída: [1]

    # Teste 4 (Pico na borda -> índice 2, valor 3)
    lista4 = [1, 2, 3]
    print(f"Lista 4: {detectar_picos(lista4)}")  # Saída: [2]

    # Teste 5 (Picos nos índices 0, 2, 6, 8 -> valores 4, 5, 4, 6)
    lista5 = [4, 3, 5, 2, 1, 2, 4, 1, 6]
    print(f"Lista 5: {detectar_picos(lista5)}")  # Saída: [0, 2, 6, 8]
