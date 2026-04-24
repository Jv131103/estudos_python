from fila import Fila

fila = Fila()


def atender():
    print("===== ATENDIMENTO =====")
    if fila.is_empty():
        print("==== NÃO HÁ FILA DE ESPERA ====")
        return
    print(f"Pessoa a ser atendida: {fila.peek()}")
    return fila.dequeue()


def adicionar():
    while True:
        print("==== ADICIONANDO ====")
        nome = input("Nome da pessoa a ser adicionada: ").strip().title()
        if not nome:
            print("==== INVÁLIDO! DIGITE UM NOME ====")
            continue
        print(f"Pessoa a ser atendida em espera: {nome} | posição na fila: {len(fila) + 1}")
        fila.enqueue(nome)
        break


def ver_proximo():
    print("==== PRÓXIMO ====")
    if fila.is_empty():
        print("==== NÃO HÁ FILA DE ESPERA ====")
        return
    prox = fila.peek()
    print(f"Próxima pessoa a ser atendida: {prox}")
    return prox


def listar_fila():
    print("==== LISTA DE ESPERA ====")
    if fila.is_empty():
        print("==== NÃO HÁ FILA DE ESPERA ====")
        return
    fila.listar()


def atendimento():
    status = [
        ["1", "atender", atender],
        ["2", "adicionar", adicionar],
        ["3", "ver próximo", ver_proximo],
        ["4", "listar", listar_fila]
    ]

    while True:
        print("==== FILA DE ATENDIMENTO ====")
        for opc1, opc2, _ in status:
            print(f"{opc1} - {opc2}")
        print("=====" * 5)

        opc = input("SITUAÇÃO ATUAL: [quit para desligar]: ").strip().lower().replace("ó", "o")
        if opc == "quit":
            print("==== FIM DO SERVIÇO ====")
            break

        for opc1, opc2, funcao in status:
            if opc == opc1 or opc == opc2:
                print()
                funcao()
                print()
                break
        else:
            print("==== OPÇÃO INVÁLIDA. DIGITE UMA OPÇÃO VÁLIDA ====")


if __name__ == "__main__":
    atendimento()
