import keyboard


def eventos_para_texto(eventos):
    saida = []
    for e in eventos:
        # só interessa quando a tecla é pressionada
        if e.event_type != "down":
            continue

        k = e.name

        # tecla de parada (a record já para no esc, mas vamos ignorar no texto)
        if k == "esc":
            continue

        # algumas teclas comuns
        if k == "space":
            saida.append(" ")
        elif k == "enter":
            saida.append("\n")
        elif k == "tab":
            saida.append("\t")
        elif k == "backspace":
            if saida:
                saida.pop()
        else:
            # letras/números/símbolos geralmente vêm como 1 caractere
            if len(k) == 1:
                saida.append(k)
            # ignora: shift, ctrl, alt, etc.

    return "".join(saida)


print("Digite em qualquer lugar. Pressione ESC para parar e mostrar o que foi digitado.")
eventos = keyboard.record(until="esc")

texto = eventos_para_texto(eventos)

print("\n=== Você digitou ===")
print(texto)
