def armadilha(lista):
    # copia = lista NÃO cria uma lista nova — apenas faz "copia" apontar
    # para o mesmo objeto na memória que "lista" já aponta.
    # Não existem duas listas aqui, existe uma lista só com dois nomes (referências).
    # Por isso, modificar "copia" também modifica "lista", e vice-versa.
    copia = lista
    lista[1] = 0
    copia.append(4)
    print("ORIGINAL:", lista)
    print("CÓPIA:", copia)


def resolver_problema1(lista):
    copia = lista.copy()
    lista[1] = 0
    copia.append(4)
    print("ORIGINAL:", lista)
    print("CÓPIA:", copia)


def resolver_problema2(lista):
    copia = lista[:]
    lista[1] = 10
    copia.append(0)
    print("ORIGINAL:", lista)
    print("CÓPIA:", copia)


def resolver_problema3(lista):
    copia = list(lista)
    lista[1] = 100
    copia.append(15)
    print("ORIGINAL:", lista)
    print("CÓPIA:", copia)


original = [1, 2, 3]
print("-- Testando armadilha --")
armadilha(original.copy())  # copia fresca, senão contamina os testes seguintes

print("-- Testando resolver_problema1 --")
resolver_problema1(original.copy())

print("-- Testando resolver_problema2 --")
resolver_problema2(original.copy())

print("-- Testando resolver_problema3 --")
resolver_problema3(original.copy())
