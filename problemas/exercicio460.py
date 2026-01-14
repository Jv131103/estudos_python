"""
Faça um programa que:

    Imprima um caminho do Windows

    Use string raw

Depois imprima o mesmo caminho sem raw e explique (comentário) o erro
"""

directory = r"C:\Users\user\Document"
print(directory)

# directory2 = "C:\Users\user\DataBases\MySQL"  # Aqui gerará erro por escape inválido, ou seja, gerará um erro de unicode por má interpretação
# print(directory2)

directory3 = "C:\\Users\\user\\PC\\Ferramentas"
print(directory3)
