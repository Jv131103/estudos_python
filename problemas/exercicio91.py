def list_is_empty(lista):
    return len(lista) <= 0


lista_maior = [
    [1, 2, 3],
    [1],
    []
]

for lista_menor in lista_maior:
    print(f"A lista {lista_menor} está vazio? {list_is_empty(lista_menor)}")
