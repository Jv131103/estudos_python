def detectar_colisao(retangulo_a, retangulo_b):
    x_a, y_a, largura_a, altura_a = retangulo_a
    x_b, y_b, largura_b, altura_b = retangulo_b

    direita_a = x_a + largura_a
    direita_b = x_b + largura_b

    cima_a = y_a + altura_a
    cima_b = y_b + altura_b

    # Separação horizontal — já está certo!
    if direita_a <= x_b or direita_b <= x_a:
        return False

    # Separação vertical — complete
    if cima_a <= y_b or cima_b <= y_a:
        return False

    return True


print(detectar_colisao((1, 1, 4, 3), (3, 2, 4, 2)))
print(detectar_colisao((0, 0, 2, 2), (5, 5, 2, 2)))
print(detectar_colisao((1, 1, 4, 3), (5, 2, 2, 2)))
print(detectar_colisao((1, 1, 4, 3), (2, 4, 2, 2)))
print(detectar_colisao((0, 0, 10, 10), (2, 2, 1, 1)))
print(detectar_colisao((1, 1, 3, 3), (1, 1, 3, 3)))
print(detectar_colisao((-3, -3, 4, 4), (0, 0, 3, 3)))
print(detectar_colisao((0, 0, 2, 2), (2, 2, 3, 3)))
