from threading import Thread


def tarefa():
    print("executando")


t = Thread(target=tarefa)
t.start()
t.join()
