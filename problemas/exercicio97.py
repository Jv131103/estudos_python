"""
Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir.
Observe que esses números são obtidos através do quadrado de cada número no
intervalo [0,9].


[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

lista = [valor**2 for valor in range(0, 10)]
print(lista)
