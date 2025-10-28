nome = "João"

print(nome)

media = 0

n1 = n2 = n3 = n4 = 0.0

nome, idade = "Jorge", 21  # Variáveis pacote, por que empacotados e desempacotados

# type: permite ver o tipo de dado
print(type(media))
print(type(nome))
print(type(n1))

# swap
n1 = 10
n2 = 9
print(n1, n2)  # Conta 10, 9

temp = n2
n2 = n1
n1 = temp
print(n1, n2)  # Com swap agra conta 9, 10

lista = [1, 2, 3]
print(lista)
lista[0], lista[2] = lista[2], lista[0]  # Mais Pythonico
print(lista)
