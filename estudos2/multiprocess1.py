from multiprocessing import Process


def tarefa():
    print("processo")


p = Process(target=tarefa)
p.start()
p.join()
