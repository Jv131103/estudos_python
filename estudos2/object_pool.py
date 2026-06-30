class ObjectPool:
    def __init__(self):
        self.pool = []

    def acquire(self):
        if self.pool:
            return self.pool.pop()
        return {}

    def release(self, obj):
        self.pool.append(obj)


pool = ObjectPool()
obj = pool.acquire()
print(obj)
pool.release(obj)
print(pool.acquire())
