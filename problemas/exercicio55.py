for i in range(5):
    for j in range(6):
        print(j)
print("FIM")


print()

for i in range(30):   # 6 números * 5 vezes = 30
    print(i % 6)
print("FIM")

print()

x = 0
for _ in range(30):
    print(x)
    x += 1
    if x == 6:
        x = 0
print("FIM")
