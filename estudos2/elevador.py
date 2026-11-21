def controlar_elevador(comandos):
    andares = {
        "andar_final": 0,
        "maior_andar": 0,
        "menor_andar": 0
    }

    inicio = 0
    i = 0
    while i < len(comandos):
        inicio += comandos[i]
        if inicio > andares["maior_andar"]:
            andares["maior_andar"] = inicio
        if inicio < andares["menor_andar"]:
            andares["menor_andar"] = inicio

        i += 1

    andares['andar_final'] = inicio

    return andares


print(controlar_elevador([3, 2, -4, 1]))
print(controlar_elevador([-2, -3, 4]))
print(controlar_elevador([5, -10, 3]))
print(controlar_elevador([]))
print(controlar_elevador([0, 0, 0]))
print(controlar_elevador([10, -5, -20, 30]))
