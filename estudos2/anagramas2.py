def sao_anagramas(str1, str2):
    if len(str1) != len(str2):
        return False

    di1 = {}
    di2 = {}

    for l1, l2 in zip(str1, str2):
        di1[l1] = di1.get(l1, 0) + 1
        di2[l2] = di2.get(l2, 0) + 1

    return di1 == di2


print(sao_anagramas("amor", "roma"))
print(sao_anagramas("arara", "aarar"))
print(sao_anagramas("casa", "caso"))
print(sao_anagramas("abc", "ab"))
