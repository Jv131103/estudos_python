def sao_anagramas(p1, p2):
    p1 = p1.lower().strip()
    p2 = p2.lower().strip()
    return sorted(p1) == sorted(p2)


print(sao_anagramas("amor", "roma"))     # True
print(sao_anagramas("python", "java"))   # False
print(sao_anagramas("Listen", "Silent"))  # True (ignore maiúsculas)
