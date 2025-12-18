def eh_par(n):
    return n & 1 == 0


for i in range(11):
    print(i, eh_par(i))
