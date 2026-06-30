class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            raise IndexError("Pilha vazia")

        return self.items.pop()

    def peek(self):
        if not self.items:
            return None

        return self.items[-1]


stack = Stack()

for i in range(5):
    stack.push(i)

print(stack.pop())
print(stack.pop())
print(stack.peek())
