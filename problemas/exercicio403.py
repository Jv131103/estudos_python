from collections import deque


def main():
    n = int(input().strip())

    fila_prioritaria = deque()
    fila_normal = deque()

    for _ in range(n):
        linha = input().rstrip()

        if linha.startswith("PRIORITARIO "):
            nome = linha[len("PRIORITARIO "):].strip()
            fila_prioritaria.append(nome)

        elif linha.startswith("NORMAL "):
            nome = linha[len("NORMAL "):].strip()
            fila_normal.append(nome)

        elif linha == "ATENDER":
            if fila_prioritaria:
                print(fila_prioritaria.popleft())
            elif fila_normal:
                print(fila_normal.popleft())
            else:
                print("SEM CLIENTES")

        elif linha == "STATUS":
            print(f"Prioritario: {len(fila_prioritaria)}")
            print(f"Normal: {len(fila_normal)}")

        else:
            # comando inesperado (não previsto no enunciado)
            pass


if __name__ == "__main__":
    main()
