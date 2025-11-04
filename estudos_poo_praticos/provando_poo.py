class Classe:
    def __init__(self, atributo1, atributo2) -> None:
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def metodo(self):
        # Mostrar quem chamou (identidade do objeto) e qual é a função compartilhada
        print(f"[metodo] self id: {id(self)}  | func id: {id(self.metodo.__func__)}")


print("1) MÉTODOS SÃO COMPARTILHADOS")
obj1 = Classe("A", 0)
obj2 = Classe("A", 1)

# Bound methods são objetos temporários diferentes a cada acesso:
print("id(obj1.metodo):", id(obj1.metodo))
print("id(obj1.metodo) (novo acesso):", id(obj1.metodo))
print("id(obj2.metodo):", id(obj2.metodo))

# ✅ Compare a FUNÇÃO, que é compartilhada:
print("id(obj1.metodo.__func__):", id(obj1.metodo.__func__))
print("id(obj2.metodo.__func__):", id(obj2.metodo.__func__))
print("id(Classe.metodo):        ", id(Classe.metodo))
print("Compartilham a MESMA função?",
      obj1.metodo.__func__ is obj2.metodo.__func__ is Classe.metodo)

# Chamadas só para ver a identidade de quem invoca e a função compartilhada
obj1.metodo()
obj2.metodo()


print("\n2) ATRIBUTOS SÃO ÚNICOS POR OBJETO (ESTADO INDEPENDENTE)")
print("Antes: obj1.atributo2 =", obj1.atributo2, "| obj2.atributo2 =", obj2.atributo2)
obj1.atributo2 = 99
print("Depois de mudar obj1.atributo2 = 99")
print("Agora: obj1.atributo2 =", obj1.atributo2, "| obj2.atributo2 =", obj2.atributo2)

# Mostrar que cada instância tem seu próprio dicionário de atributos
print("id(obj1.__dict__):", id(obj1.__dict__), "| id(obj2.__dict__):", id(obj2.__dict__))


print("\n3) VARIÁVEIS NÃO SÃO OBJETOS (SÃO REFERÊNCIAS A OBJETOS)")
# Exemplo com imutável (int): rebind cria outro objeto
x = 10
y = x
print("int: id(x) == id(y)?", id(x) == id(y))  # mesmo objeto 10
y = 11  # y agora referencia OUTRO objeto
print("Depois de y = 11 → id(x) == id(y)?", id(x) == id(y))

# Exemplo com mutável (list): duas variáveis apontam pro MESMO objeto
a = [1]
b = a
print("list: id(a) == id(b)?", id(a) == id(b))
b.append(2)
print("Após b.append(2), a =", a, "| b =", b, "(ambas mudaram, é o MESMO objeto)")
# Rebinding: agora b aponta pra OUTRA lista, a permanece
b = [1, 2, 3]
print("Depois de b = [1,2,3] → a =", a, "| b =", b, "| id(a) == id(b)?", id(a) == id(b))
