
def parenteses_validos(texto):
    pilha = []
    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in texto:
        if char in "([{":
            pilha.append(char)

        elif char in ")]}":
            if not pilha:
                return False

            topo = pilha.pop()
            if topo != pares[char]:
                return False

    return len(pilha) == 0


print(parenteses_validos("()"))
print(parenteses_validos("([])"))
print(parenteses_validos("([{}])"))
print(parenteses_validos("(]"))
print(parenteses_validos("((())"))
print(parenteses_validos(")("))
