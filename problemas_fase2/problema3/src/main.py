def compactar(texto: str) -> str:
    """
    tempo: O(n)
    Espaço: O(n)
    """

    if not isinstance(texto, str):
        raise ValueError("param texto precisa ser do tipo str")

    if not texto:
        return texto

    anterior = texto[0]
    new = []

    cont = 0
    for valor in texto:
        if valor == anterior:
            cont += 1
        else:
            new.append(f"{anterior}{cont}")
            cont = 1
            anterior = valor

    new.append(f"{anterior}{cont}")

    compactado = "".join(new)

    return compactado if len(compactado) < len(texto) else texto


def compactar2(texto: str) -> str:
    """
    tempo = O(n)
    espaço = O(n)
    """
    if not isinstance(texto, str):
        raise TypeError("texto deve ser str")

    if not texto:
        return texto

    anterior = texto[0]
    cont = 0
    partes = []
    append = partes.append

    for valor in texto:
        if valor == anterior:
            cont += 1
        else:
            append(anterior)
            append(str(cont))
            anterior = valor
            cont = 1

    append(anterior)
    append(str(cont))

    compactado = "".join(partes)
    return compactado if len(compactado) < len(texto) else texto


def descompactar(compactado: str) -> str:
    """
    Parsing do compactado: O(n) (n = len(compactado))

    Construção da saída: O(m) (m = tamanho do texto descompactado)

    Total: O(n + m), que é o correto (não tem como escapar do m).
    """
    if not isinstance(compactado, str):
        raise TypeError("compactado deve ser str")
    if not compactado:
        return compactado

    res = []
    i = 0
    n = len(compactado)

    while i < n:
        ch = compactado[i]
        i += 1

        # Se acabou e não veio número, devolve como está (não parece compactado)
        if i >= n or not compactado[i].isdigit():
            return compactado

        # Lê número com vários dígitos (ex: 12, 300, ...)
        num = 0
        while i < n and compactado[i].isdigit():
            num = num * 10 + (ord(compactado[i]) - 48)
            i += 1

        # Repete
        res.append(ch * num)

    return "".join(res)


if __name__ == "__main__":
    print(compactar2("aaabbcdddd"))
    print(descompactar("a3b2c1d4"))
    print(compactar2("aaaaaaaaaaaaaaaaaabbbbbbbccccddddeeeeeeeeeeeeeeeee"))
    print(descompactar("a18b7c4d4e17"))
    print(compactar2("abcd"))
    print(descompactar("abcd"))
    print(compactar2("aabb"))
    print(descompactar("aabb"))
