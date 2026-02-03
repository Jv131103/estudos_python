from multiprocessing import Process, Queue


def produtor(q):
    q.put(42)


if __name__ == "__main__":
    q = Queue()
    p = Process(target=produtor, args=(q,))
    p.start()
    print(q.get())
    p.join()
