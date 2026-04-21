import itertools
import string

senha_correta = "Ab"

caracteres = string.ascii_letters + string.digits + string.punctuation

for tentativa in itertools.product(caracteres, repeat=2):
    tentativa = ''.join(tentativa)

    print("Testando:", tentativa)

    if tentativa == senha_correta:
        print("Senha encontrada:", tentativa)
        break
