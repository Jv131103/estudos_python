def intersecao(a, b):
    a = sorted(a)
    b = sorted(b)

    i = j = 0
    res = []

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    return res


l1 = [1, 2, 3]
l2 = [3, 4, 5, 6]

i = intersecao(l1, l2)
print(i)
