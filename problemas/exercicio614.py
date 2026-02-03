"""
Crie um script que:

    configure o locale para pt-BR
    imprima a data atual por extenso
    imprima o valor 1999.90 em reais

"""

import locale
from datetime import datetime

# Configurando locale pt-BR (com fallback)
try:
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
except locale.Error:
    locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")


hoje = datetime.now()
data_extenso = hoje.strftime("%d de %B de %Y")
print(data_extenso)

valor = float(input("Valor: "))
print(locale.currency(valor, grouping=True))
