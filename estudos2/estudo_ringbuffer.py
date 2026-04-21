dados = [None] * 4  # tamanho fixo
inicio = 0
fim = 0
qtd = 0
tamanho = 4


def enqueue_sem_tratamento(valor):
    """Precisa da função dequeue para funcionar corretamente"""
    global fim, qtd
    dados[fim] = valor
    fim = (fim + 1) % tamanho
    qtd += 1


def enqueue_limitado(valor):
    global fim, qtd
    if qtd == tamanho:
        raise OverflowError("Buffer cheio")

    dados[fim] = valor
    fim = (fim + 1) % tamanho
    qtd += 1


def enqueue_circular(valor):
    """Sobrescreve corretamente sem erro lógico"""
    global fim, qtd, inicio
    dados[fim] = valor
    fim = (fim + 1) % tamanho

    if qtd < tamanho:
        qtd += 1
    else:
        inicio = (inicio + 1) % tamanho


def dequeue():
    """Usado no caso da primeira função para torná-la circular
    sem bugs lógicos de sobrescrita"""
    global inicio, qtd
    valor = dados[inicio]
    dados[inicio] = None
    inicio = (inicio + 1) % tamanho
    qtd -= 1
    return valor


for i in range(10):
    enqueue_circular(i)
    print(dados)


'''print(dados)

print(dequeue())
enqueue(i + 1)
print(dados)

dequeue()
enqueue(i + 2)
print(dados)
'''
