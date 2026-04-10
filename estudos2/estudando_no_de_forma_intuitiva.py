a = {"valor": "a", "prox": None}
b = {"valor": "b", "prox": None}
c = {"valor": "c", "prox": None}

a["prox"] = b
b["prox"] = c


def ler():
    atual = a
    while atual:
        print(atual["valor"])
        atual = atual["prox"]


def inserir(valor):
    global a

    if not a:
        a = {"valor": valor, "prox": None}
        return

    novo = a
    while True:
        if novo["prox"] is None:
            novo["prox"] = {"valor": valor, "prox": None}
            break
        novo = novo["prox"]


def inserir_inicio(valor):
    global a
    a = {"valor": valor, "prox": a}


def contar_nos():
    atual = a
    cont = 0

    while atual:
        cont += 1
        atual = atual["prox"]

    print(f"HÁ: {cont} Nós")
    return cont


def buscar_valor(valor):
    atual = a

    while atual:
        if atual["valor"] == valor:
            return atual
        atual = atual["prox"]
    return None


def remover(valor):
    global a

    if not a:
        return None

    # caso especial: remover a cabeça
    if a["valor"] == valor:
        a = a["prox"]
        return

    anterior = a
    atual = a["prox"]

    while atual:
        if atual["valor"] == valor:
            anterior["prox"] = atual["prox"]
            return
        anterior = atual
        atual = atual["prox"]


def encontrar_meio():
    slow = a
    fast = a

    while fast and fast["prox"]:
        slow = slow["prox"]
        fast = fast["prox"]["prox"]

    return slow


def tem_ciclo():
    slow = a
    fast = a

    while fast and fast["prox"]:
        slow = slow["prox"]
        fast = fast["prox"]["prox"]

        if slow == fast:
            return True

    return False


inserir("d")
inserir("e")
ler()
contar_nos()
print(buscar_valor("c"), buscar_valor("f"))
inserir_inicio("0")
inserir_inicio("batata")
ler()
print(buscar_valor("0"), buscar_valor("a"))
remover("d")
remover("batata")
remover("e")
ler()
print(encontrar_meio())

# Teste em que ciclo == True
# ultimo = buscar_valor("c")
# segundo = buscar_valor("a")
# ultimo["prox"] = segundo
print(tem_ciclo())
