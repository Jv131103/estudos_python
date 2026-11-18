def mover_robo(comandos):
    x = 0
    y = 0

    for comando in comandos:
        if comando == "C":
            y += 1
        elif comando == "B":
            y -= 1
        elif comando == "D":
            x += 1
        elif comando == "E":
            x -= 1
        else:
            print("Posicao inválida, robô parado")

    return x, y


print(mover_robo(["D", "D", "C", "E"]))
print(mover_robo(["C", "D", "B", "E"]))
print(mover_robo(["B", "B", "B"]))
print(mover_robo([]))
print(mover_robo(["D", "D", "D", "C", "C", "E", "B"]))
print(mover_robo(["E", "E", "C", "C", "D", "B"]))
