def calcular_media(notas):
    if not isinstance(notas, list):
        raise TypeError("Tipo inválido, digite apenas listas")

    soma = 0
    qtd = 0

    for valor in notas:
        soma += valor
        qtd += 1

    return soma / qtd


def situacao(media):
    if not isinstance(media, (int, float)):
        raise TypeError("Tipo inválido, digite apenas Números")

    table = [
        [7, 10, "Aprovado"],
        [5, 6.9, "Recuperação"],
        [0, 4.9, "Reprovado"]
    ]

    for dados in table:
        nota_menor, nota_maior, status = dados
        if nota_menor <= media <= nota_maior:
            return status
    return None


def ordenar_notas(notas):
    if not isinstance(notas, list):
        raise TypeError("Tipo inválido, digite apenas listas")

    if len(notas) <= 1:
        return notas

    pivot = notas[len(notas) // 2]

    left = [x for x in notas if x < pivot]
    middle = [x for x in notas if x == pivot]
    right = [x for x in notas if x > pivot]

    return ordenar_notas(left) + middle + ordenar_notas(right)


def maior_e_menor(notas):
    if not isinstance(notas, list):
        raise TypeError("Tipo inválido, digite apenas listas")

    ordenada = ordenar_notas(notas)
    menor = ordenada[0]
    maior = ordenada[-1]
    return menor, maior


def pedir_float(message):
    while True:
        try:
            return float(input(message).replace(",", "."))
        except ValueError:
            print("Digite apenas números!")


def main():
    bucket_notas = []
    qtd = 1
    while True:
        nota = pedir_float(f"Nota {qtd}: [-1 para sair] ")
        if nota == -1:
            break
        bucket_notas.append(nota)

    media = calcular_media(bucket_notas)
    status = situacao(media)
    notas_ordenadas = ordenar_notas(bucket_notas)
    menor, maior = maior_e_menor(bucket_notas)

    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")
    print(f"Notas ordenadas: {notas_ordenadas}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")


if __name__ == "__main__":
    main()
