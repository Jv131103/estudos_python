"""
Faça um programa que:

    Receba uma lista de números inteiros entre 0 e 99

    Crie 10 buckets, cada um representando uma faixa:

        0–9

        10–19

        20–29

        …

        90–99

    Distribua os números nos buckets corretos

    Mostre cada bucket com sua faixa

Exemplo conceitual:

    Entrada: [3, 17, 25, 42, 8, 91]
    Bucket 0–9   → [3, 8]
    Bucket 10–19 → [17]
    Bucket 20–29 → [25]
    Bucket 40–49 → [42]
    Bucket 90–99 → [91]
"""


def bucket(lista):
    data = {
        "0-9": [],
        "10-19": [],
        "20-29": [],
        "30-39": [],
        "40-49": [],
        "50-59": [],
        "60-69": [],
        "70-79": [],
        "80-89": [],
        "90-99": [],
        "garbage": []
    }

    for valor in lista:
        if 0 <= valor <= 9:
            data["0-9"].append(valor)
        elif 10 <= valor <= 19:
            data["10-19"].append(valor)
        elif 20 <= valor <= 29:
            data["20-29"].append(valor)
        elif 30 <= valor <= 39:
            data["30-39"].append(valor)
        elif 40 <= valor <= 49:
            data["40-49"].append(valor)
        elif 50 <= valor <= 59:
            data["50-59"].append(valor)
        elif 60 <= valor <= 69:
            data["60-69"].append(valor)
        elif 70 <= valor <= 79:
            data["70-79"].append(valor)
        elif 80 <= valor <= 89:
            data["80-89"].append(valor)
        elif 90 <= valor <= 99:
            data["90-99"].append(valor)
        else:
            data["garbage"].append(valor)

    return data


def bucket_otimizado(lista):
    data = {f"{i * 10}-{i * 10 + 9}": [] for i in range(10)}
    data["garbage"] = []

    for valor in lista:
        if 0 <= valor <= 99:
            idx = valor // 10
            chave = f"{idx * 10}-{idx * 10 + 9}"
            data[chave].append(valor)
        else:
            data["garbage"].append(valor)

    return data


print(bucket([3, 17, 25, 42, 8, 91]))
print(bucket_otimizado([3, 17, 25, 42, 8, 91]))
