class MeuInt(int):
    pass


y = MeuInt(5)

print(type(y) is int)  # False. verifica se o tipo é exatamente int. Nesse caso não é do tipo int
print(isinstance(y, int))   # True. verifica se o objeto é do tipo int ou de uma subclasse de int. Nesse caso, é subclass de int
