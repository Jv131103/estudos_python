def remover_repeticoes(texto):

    result = {
        'texto': "",
        'removidos': 0
    }
    if not texto:
        return result

    antes = texto[0]
    for i in range(1, len(texto)):
        if texto[i] == antes:
            result["removidos"] += 1
        else:
            result["texto"] += antes

        antes = texto[i]

    result['texto'] += antes

    return result


print(remover_repeticoes("aaabbccccdaa"))
print(remover_repeticoes("banana"))
print(remover_repeticoes("aabbcc"))
print(remover_repeticoes("aaaaa"))
print(remover_repeticoes("AAbbA"))
print(remover_repeticoes(""))
print(remover_repeticoes("1122333"))
