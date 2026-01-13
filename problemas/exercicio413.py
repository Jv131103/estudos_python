"""
Considere:

    class A: pass
    class B(A): pass


Responda:

    issubclass(B, A)

    isinstance(B(), A)

    type(B()) == A

"""


class A:
    pass


class B(A):
    pass


print(issubclass(B, A))
print(isinstance(B(), A))
print(type(B()) == A)
