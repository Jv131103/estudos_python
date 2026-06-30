# Queremos trocar o elemento da posição 0 com o da posição 1 manualmente
valores = [99, 5]

# Se fizermos: valores[0] = valores[1], a lista vira [5, 5] e perdemos o 99 para sempre.

copo_auxiliar = valores[0]  # <-- AUXILIAR (salva o 99 antes que ele seja apagado)
valores[0] = valores[1]     # Posição 0 recebe o 5. Lista vira: [5, 5]
valores[1] = copo_auxiliar  # Posição 1 recebe o 99 guardado. Lista vira: [5, 99]

print("Lista invertida com sucesso:", valores)
