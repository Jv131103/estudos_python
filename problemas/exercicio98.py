"""
Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir.
Observe que esses números são obtidos através da raiz quadrada de cada número
no intervalo [1,50]. Utilize round() para arredondar as casas decimais.


    [1.0, 1.41, 1.73, 2.0, 2.24, 2.45, 2.65, 2.83, 3.0, 3.16, 3.32, 3.46,
    3.61, 3.74, 3.87, 4.0, 4.12, 4.24, 4.36, 4.47, 4.58, 4.69, 4.8, 4.9,
    5.0, 5.1, 5.2, 5.29, 5.39, 5.48, 5.57, 5.66, 5.74, 5.83, 5.92, 6.0,
    6.08, 6.16, 6.24, 6.32, 6.4, 6.48, 6.56, 6.63, 6.71, 6.78, 6.86,
    6.93, 7.0, 7.07]

"""
lista = [round(valor**(1 / 2), 2) for valor in range(1, 51)]
print(lista)
