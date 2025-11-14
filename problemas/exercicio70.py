lista = [
    (1,),
    [1, 2, 3],
    (1),
    {4, 5},
    {'nome': 'A', 'value': 2},
    10,
    [],
    1 + 3j,
    1.2,
    True,
    False,
    None,
    'Hello World!',
]

for itens in lista:
    print(f"Informação para valor {itens}")
    print(f"Tipo completo: {type(itens)}")
    print(f"Tipo resumido: {type(itens).__name__}")
    print(f"Endereço de memória referenciado: {id(itens)}")
    print(f"Funcionalidade: {dir(itens)}")
    print()
