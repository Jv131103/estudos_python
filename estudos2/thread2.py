from threading import Thread


def minha_funcao(n):
    print("rodando", n)


t = Thread(target=minha_funcao, args=(10,))
t.start()
t.join()
