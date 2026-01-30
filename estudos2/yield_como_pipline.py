def gera_1_a_20():
    for n in range(1, 21):
        yield n


def filtra_multiplos_de_3(gerador):
    for n in gerador:
        if n % 3 == 0:
            yield n


def quadrado(gerador):
    for n in gerador:
        yield n * n


# Consumo final
pipeline = quadrado(filtra_multiplos_de_3(gera_1_a_20()))

for valor in pipeline:
    print(valor)
