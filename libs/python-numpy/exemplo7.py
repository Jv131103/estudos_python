import numpy as np

# Determinante e inversa
# São cálculos fundamentais em álgebra linear, sendo usados
# para resolver sistemas de equações e entender propriedades
# de tranformações lineares.
# Determinate é um valor escalar que pode indicar se uma matriz
# é um valor escalar que pode indicar se uma amtriz é invertível,
# caso seu valor seja diferente de zero
# A matriz inversa, por sua vez, é utilizada para resolver
# equações do tipo. Ax = b
a = np.array([[1, 2], [3, 4]])

# Determinante
det = np.linalg.det(a)
print(f"Determinate da matriz: {det}")

# Inversa
inv = np.linalg.inv(a)
print(f"Inversa da matriz: {inv}")
