def hanoi(n, origem, destino, auxiliar):

    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return

    hanoi(n - 1, origem, auxiliar, destino)

    print(f"Mover disco {n} de {origem} para {destino}")

    hanoi(n - 1, auxiliar, destino, origem)


hanoi(3, "A", "C", "B")
