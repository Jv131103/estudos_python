def controlar_video(estado_inicial, comandos):
    estado_atual = estado_inicial
    recusas = 0

    for comando in comandos:
        if estado_atual == "parado" and comando == "tocar":
            estado_atual = "tocando"
        elif estado_atual == "tocando" and comando == "pausar":
            estado_atual = "pausado"
        elif estado_atual == "pausado" and comando == "continuar":
            estado_atual = "tocando"
        elif estado_atual in ["tocando", "pausado"] and comando == "parar":
            estado_atual = "parado"
        else:
            recusas += 1

    return estado_atual, recusas


def controlar_video2(estado_inicial, comandos):
    estado_atual = estado_inicial
    recusas = 0

    tabela = {
        ("parado", "tocar"): "tocando",
        ("tocando", "pausar"): "pausado",
        ("pausado", "continuar"): "tocando",
        ("tocando", "parar"): "parado",
        ("pausado", "parar"): "parado"
    }

    for comando in comandos:
        item = (estado_atual, comando)
        if item in tabela:
            estado_atual = tabela[item]
        else:
            recusas += 1

    return estado_atual, recusas


print(controlar_video(
    "parado",
    ["tocar", "pausar", "continuar", "parar"]
))
print(controlar_video(
    "parado",
    ["pausar", "tocar", "pausar", "continuar", "parar"]
))
print(controlar_video("tocando", []))
print(controlar_video(
    "parado",
    ["parar", "continuar"]
))
print(controlar_video(
    "pausado",
    ["continuar", "pausar"]
))
print(controlar_video(
    "tocando",
    ["tocar", "parar", "pausar"]
))
print()
print(controlar_video2(
    "parado",
    ["tocar", "pausar", "continuar", "parar"]
))
print(controlar_video2(
    "parado",
    ["pausar", "tocar", "pausar", "continuar", "parar"]
))
print(controlar_video2("tocando", []))
print(controlar_video2(
    "parado",
    ["parar", "continuar"]
))
print(controlar_video2(
    "pausado",
    ["continuar", "pausar"]
))
print(controlar_video2(
    "tocando",
    ["tocar", "parar", "pausar"]
))
