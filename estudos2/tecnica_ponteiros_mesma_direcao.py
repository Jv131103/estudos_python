lista = [10, 20, 30, 40, 50, 60]


def percorrer_simples():
    slow = 0
    fast = 0

    while fast < len(lista):
        print(f"slow={lista[slow]}, fast={lista[fast]}")

        slow += 1          # anda 1
        fast += 2          # anda 2


def meio_lista(lista):
    slow = 0
    fast = 0

    while fast < len(lista) and fast + 1 < len(lista):
        slow += 1
        fast += 2

    return lista[slow]


def maior_substring(s):
    vistos = set()
    slow = 0
    maior = 0

    for fast in range(len(s)):
        while s[fast] in vistos:
            vistos.remove(s[slow])
            slow += 1

        vistos.add(s[fast])
        maior = max(maior, fast - slow + 1)

    return maior


percorrer_simples()
print(meio_lista(lista))
print(maior_substring("teste"))
