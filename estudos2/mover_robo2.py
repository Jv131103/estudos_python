def controlar_robo(comandos):
    direcoes = ["N", "L", "S", "O"]

    x = 0
    y = 0
    indice = 1  # Começa olhando para Leste

    for comando in comandos:

        if comando == "D":  # Gira 90° para a direita
            indice = (indice + 1) % 4

        elif comando == "E":  # Gira 90° para a esquerda
            indice = (indice - 1) % 4

        elif comando == "F":  # Avança uma casa para a frente
            direcao = direcoes[indice]

            if direcao == "N":
                y += 1
            elif direcao == "S":
                y -= 1
            elif direcao == "L":
                x += 1
            elif direcao == "O":
                x -= 1

    return x, y, direcoes[indice]


print(controlar_robo(["F", "F", "D", "F"]))
print(controlar_robo(["E", "F", "D", "F"]))
print(controlar_robo(["D", "D", "F"]))
print(controlar_robo(["E", "E", "F"]))
print(controlar_robo(["F", "D", "F", "D", "F", "D", "F"]))
print(controlar_robo([]))
