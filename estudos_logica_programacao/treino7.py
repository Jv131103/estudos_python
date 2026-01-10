def exercicio_logico(x, y, z):
    # validação: qualquer um fora da faixa 1..3
    if not (1 <= x <= 3) or not (1 <= y <= 3) or not (1 <= z <= 3):
        print("Erro: x, y e z precisam estar entre 1 e 3.")
        return

    e1 = (x == y) and (y <= 2) and (z == y + 1)
    e2 = (x == y) or (y <= 2) or (z == y + 1)
    e3 = (x == y) and (y <= 2) or (z == y + 1)          # AND antes do OR
    e4 = (x == y) or (y <= 2) and (z == y + 1)          # AND antes do OR
    e5 = (x == y) and ((y <= 2) or (z == y + 1))
    e6 = ((x == y) or (y <= 2)) and (z == y + 1)

    print(f"x={x}, y={y}, z={z}")
    print(f"1) {e1}")
    print(f"2) {e2}")
    print(f"3) {e3}")
    print(f"4) {e4}")
    print(f"5) {e5}")
    print(f"6) {e6}")


exercicio_logico(1, 2, 3)
exercicio_logico(2, 1, 3)
