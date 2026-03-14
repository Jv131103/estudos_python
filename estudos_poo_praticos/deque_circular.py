class CircularDeque:
    def __init__(self, k):
        self.buffer = [None] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value):

        if self.isFull():
            return False

        self.head = (self.head - 1) % self.capacity
        self.buffer[self.head] = value
        self.size += 1

        return True

    def insertLast(self, value):

        if self.isFull():
            return False

        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

        return True

    def deleteFront(self):

        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1

        return True

    def deleteLast(self):

        if self.isEmpty():
            return False

        self.tail = (self.tail - 1) % self.capacity
        self.size -= 1

        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.buffer[self.head]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.buffer[(self.tail - 1) % self.capacity]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


dc = CircularDeque(5)
dc.insertFront(1)
dc.insertFront(2)
dc.insertFront(3)
dc.insertLast(1)
dc.insertLast(2)
print(dc.buffer)
print(dc.getFront(), dc.getRear())
print(dc.deleteFront(), dc.deleteLast())
