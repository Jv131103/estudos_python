a = 6
b = 10
c = 2

if a + b > c:
    c = b * c
elif a != b and b != c:
    b = a + c

if a == b or b == c:
    a = b - 1
else:
    a = b + 1
    b = c + 1
    c = a + 1

print(f"{a=} | {b=} | {c=}")
