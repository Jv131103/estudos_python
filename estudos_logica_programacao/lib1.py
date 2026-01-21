
# Desenvolvido por prof. Marcio Feitosa

import random


def dentroDosLimites(mat, l, c):
    if l < 0 or l >= len(mat) or c < 0 or c >= len(mat[0]):
        return False
    return True


def pausa():
    input("\nPressione ENTER para continuar")


def imprimeMatrizNaVertical(m):
    for linha in range(len(m)):
        for coluna in range(len(m[0])):
            print('[', linha, '][', coluna, '] = ', m[linha][coluna])


def imprimeMatrizLinhaALinha(m):
    for linha in range(len(m)):
        print('')
        for coluna in range(len(m[0])):
            print(m[linha][coluna], end=" ")


def preencheMatriz(m, min, max):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = random.randint(min, max)
    return m


def localizaValor(m, v):
    ret = '{'
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == v:
                ret += ' [' + str(i) + '][' + str(j) + ']'
    return ret + ' }'


def contabilizaMaiores(m, v):
    cont = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] >= v:
                cont += 1
    return cont


def contabilizaIguais(m, v):
    cont = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == v:
                cont += 1
    return cont
