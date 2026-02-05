
# Desenvolvido por prof. Marcio Feitosa

import lib1

lin = int(input("Quantidade de  linhas: "))
col = int(input("Quantidade de colunas: "))

mat = [[0] * col for _ in range(lin)]

min = int(input("Valor aleatório mínimo: "))
max = int(input("Valor aleatório máximo: "))

lib1.preencheMatriz(mat, min, max)

while True:
    print("-------------------------------------------------------------------")
    print("               PROGRAMA PARA ESTUDO DA MATRIZ")
    print("-------------------------------------------------------------------")
    print("0 - encerrar")
    print("1 - ler o conteúdo de uma célula")
    print("2 - alterar o conteudo de uma célula")
    print("3 - trocar o conteúdo de uma célula com outra (operação 'swap')")
    print("4 - localizar um valor na matriz")
    print("5 - contabilizar valores maiores ou iguais a determinado valor")
    print("6 - imprimir a matriz na vertical")
    print("7 - imprimir a matriz a cada linha inteira")
    print("8 - trocar todos os valores de uma linha com outra")
    print("9 - preencher com novos números aleatórios")
    print("-------------------------------------------------------------------")
    opc = int(input("Sua opção: "))

    if opc == 0:
        break

    elif opc == 1:
        print("Forneça as coordenadas")
        l = int(input("->  linha: "))
        c = int(input("-> coluna: "))
        if not lib1.dentroDosLimites(mat, l, c):
            print("Fora dos limites da matriz")
            lib1.pausa()
            continue

        print("Conteúdo da linha", str(l), " e coluna", str(c), "é ", str(mat[l][c]))
        lib1.pausa()

    elif opc == 2:
        print("Forneça as coordenadas")
        l = int(input("->  linha: "))
        c = int(input("-> coluna: "))
        if not lib1.dentroDosLimites(mat, l, c):
            print("Fora dos limites da matriz")
            lib1.pausa()
            continue
        v = int(input("Forneça o novo valor: "))
        if v < min or v > max:
            print("Fora da faixa dos valores aleatórios.")
            lib1.pausa()
            continue
        mat[l][c] = v
        print("O valor foi alterado.")
        lib1.pausa()

    elif opc == 3:
        print("Forneça as coordenadas da célula 1")
        l1 = int(input("->  linha: "))
        c1 = int(input("-> coluna: "))
        print("Forneça as coordenadas da célula 2")
        l2 = int(input("->  linha: "))
        c2 = int(input("-> coluna: "))
        if not lib1.dentroDosLimites(mat, l1, c1) or not lib1.dentroDosLimites(mat, l2, c2):
            print("Alguma das coordenadas está fora dos limites da matriz")
            lib1.pausa()
            continue
        if l1 == l2 and c1 == c2:
            print("Trata-se da mesma célula")
            lib1.pausa()
            continue

        temp = mat[l2][c2]  # salvar temporariamente o conteúdo de uma das células
        mat[l2][c2] = mat[l1][c1]  # sobrescrever o conteúdo desta última célula com o da primeira
        mat[l1][c1] = temp  # sobrescrever o conteúdo da primeira com o conteúdo salvo da segunda

        print("Conteúdo trocado.")
        if mat[l1][c1] == mat[l2][c2]:
            print("Observação: Os conteúdos das células são iguais. Se for imprimir, não perceberá a diferença.")
        lib1.pausa()

    elif opc == 4:
        v = int(input("Valor que deseja encontrar: "))
        if v < min or v > max:
            print("Valor fora da faixa definida inicialmente.")
        # cont = lib1.contabilizaIguais(mat, v)
        # print("Encontrados: ",cont, " iguais.")
        print("Posições dos valores encontrados [linha][coluna] =", end=" ")
        print(lib1.localizaValor(mat, v))
        lib1.pausa()

    elif opc == 5:
        v = int(input("Valor que deseja encontrar: "))
        if v < min or v > max:
            print("Valor fora da faixa definida inicialmente.")
        cont = lib1.contabilizaMaiores(mat, v)
        print("Encontrados: ", cont, " maiores ou iguais.")
        lib1.pausa()

    elif opc == 6:
        lib1.imprimeMatrizNaVertical(mat)
        lib1.pausa()

    elif opc == 7:
        lib1.imprimeMatrizLinhaALinha(mat)
        lib1.pausa()

    elif opc == 8:
        print("Forneça as linhas que deseja trocar")
        l1 = int(input("-> linha 1: "))
        l2 = int(input("-> linha 2: "))

        # valida apenas as linhas (coluna 0 só para checagem)
        if not lib1.dentroDosLimites(mat, l1, 0) or not lib1.dentroDosLimites(mat, l2, 0):
            print("Alguma das linhas está fora dos limites da matriz")
            lib1.pausa()
            continue

        if l1 == l2:
            print("Trata-se da mesma linha")
            lib1.pausa()
            continue

        # swap de linha inteira
        mat[l1], mat[l2] = mat[l2], mat[l1]

        print("Linhas trocadas com sucesso.")
        lib1.pausa()

    elif opc == 9:
        lib1.preencheMatriz(mat, min, max)
        print("A matriz foi preenchida com novos valore.")
        lib1.pausa()

print("\n\nObrigado pela utilização do Programa para Estudo da Matriz. Até a próxima.\n\n")
