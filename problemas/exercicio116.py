def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return n
    return n * fatorial_recursivo(n - 1)


lista = ['A', 'B', 'C', 'D', 'E']
dicionario = {valor: fatorial_recursivo(i) for i, valor in enumerate(lista, start=1)}
print(dicionario)
