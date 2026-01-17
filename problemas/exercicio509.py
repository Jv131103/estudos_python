"""
Faça um programa que:

    . Leia:

        . idade

        . possui_documento (bool)

        . horário (0–23)

    . Use tabela de decisão para determinar:

        . "Entrada liberada"

        . "Entrada proibida"

    Regras:

        Menor de 16 → proibido
        16–17 → só com documento
        18+ → liberado apenas entre 8h e 22h

    Evite if combinatórios.

    Use pré-processamento + tabela.
"""

# Pré-processar estados simples
idade = int(input("Idade: "))
possui_documento = input("Possui documento? [y/n] ").lower() == "y"
horario = int(input("Horário (0–23): "))

menor_16 = idade < 16
faixa_16_17 = 16 <= idade <= 17
maior_18 = idade >= 18
horario_permitido = 8 <= horario <= 22

# Reduzir para UM estado decisório
estado = (
    menor_16,
    faixa_16_17,
    maior_18,
    possui_documento,
    horario_permitido
)

# Tabela de decisão REAL
tabela = {
    # menor de 16
    (True, False, False, False, False): "Entrada proibida",
    (True, False, False, True, True): "Entrada proibida",

    # 16–17
    (False, True, False, True, True): "Entrada liberada",
    (False, True, False, False, True): "Entrada proibida",

    # 18+
    (False, False, True, True, True): "Entrada liberada",
    (False, False, True, True, False): "Entrada proibida",
}

print(tabela.get(estado, "Entrada proibida"))
