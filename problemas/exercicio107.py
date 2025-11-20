frutas = ['  BaNanA    ', '  morangO ', ' mAçã  ', '   MeLão']

eu_gosto = [f"Eu gosto de {fruta.strip().capitalize()} !" for fruta in frutas]
print(eu_gosto)

maiusculas = [fruta.strip().upper() for fruta in frutas]
print(maiusculas)

minusculas = [fruta.strip().lower() for fruta in frutas]
print(minusculas)
