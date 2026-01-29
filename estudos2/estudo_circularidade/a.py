print("importando a.py...")

# from b import func_b  # <-- importa b.py


def func_a():
    from b import func_b
    return "func_a chamou -> " + func_b()
