linguagens = ["php", "JavaScript"]
frases = ['Eu amo ', 'Eu odeio ']


lista_frases = []
for linguagem in linguagens:
    for frase in frases:
        lista_frases.append(frase + linguagem + " !")
print(lista_frases)

lista_frases2 = []
for linguagem in linguagens:
    for frase in frases:
        lista_frases2.append(f"{frase} {linguagem} !")
print(lista_frases2)

lista_frase3 = []
for indice_lp in range(len(linguagens)):
    for indice_txt in range(len(frases)):
        lista_frase3.append(frases[indice_txt] + linguagens[indice_lp] + " !")
print(lista_frase3)
