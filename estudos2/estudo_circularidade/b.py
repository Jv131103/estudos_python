print("importando b.py...")

from a import func_a  # <-- importa a.py de volta (ciclo)


def func_b():
    return "func_b"


print(func_a())
