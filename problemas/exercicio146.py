var1 = ['Hello World!']
var2 = True and all([True or False, ()])
var3 = ('10',) if 10 > 4 else 1
var4 = ('Hello World!')
var5 = ('Python is love!',)

print(f"{var1} - {type(var1)}")
print(f"{var2} - {type(var2)}")
print(f"{var3} - {type(var3)}")
print(f"{var4} - {type(var4)}")
print(f"{var5} - {type(var5)}")

print()

var6 = [var1, var2, var3, var4, var5]

for var in var6:
    print(var, "É tupla" if isinstance(var, tuple) else "Não é tupla")
