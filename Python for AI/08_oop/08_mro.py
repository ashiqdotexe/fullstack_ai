class A:
    label = "A: base tea"
class B(A):
    label = "B: masala tea"
class C(A):
    label = "C: flavor tea"
class D(B, C):
    pass

cup = D()
print(cup.label) # It will call the B, because it comes first in serial
print(D.__mro__) # There is also Dunder for mro as well(__mro__)