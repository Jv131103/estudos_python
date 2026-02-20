j = 0

for i in range(0, 5, 1):
    while j < 5:
        if i < 3:
            j += 3
        else:
            j += 1
print(f"j = {j}")
