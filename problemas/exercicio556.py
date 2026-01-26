"""
Validação de regras com conjuntos

Faça um programa que:

    Defina um conjunto de permissões obrigatórias

    Leia um conjunto de permissões de um usuário

    Verifique se:

        o usuário tem todas as permissões obrigatórias

        se existem permissões extras

    Mostre o resultado de forma clara

Exemplo conceitual:

    Obrigatórias: {"ler", "escrever"}
    Usuário: {"ler", "executar"}

DICAS:

    Use <= (subconjunto)

    Use - para permissões extras

    set é ideal para validação
"""

obrigatorias = {"ler", "escrever"}
usuario = {"ler", "escrever", "executar"}

# Verifica se tem todas as obrigatórias
if obrigatorias <= usuario:
    print("Usuário possui todas as permissões obrigatórias")
else:
    print("Usuário NÃO possui todas as permissões obrigatórias")

# Verifica permissões extras
extras = usuario - obrigatorias
if extras:
    print("Permissões extras:", extras)
else:
    print("Nenhuma permissão extra")
