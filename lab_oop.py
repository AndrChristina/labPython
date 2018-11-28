#Python. Лабораторна робота _oop. Андріїшин Христина, FI-9119
print('Python. Лабораторна робота _oop')
print('Андріїшин Христина, FI-9119')
from math import*
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return str(self.a)+'+'+str(self.b)+'i' 
    def __add__(self, rhs):
        return Complex(self.a+rhs.a, self.b+rhs.b)
    def __sub__(self, rhm):
        return Complex(self.a-rhm.a, self.b-rhm.b)
    def __mul__(self, rhn):
        return Complex(self.a*rhn.a-self.b*rhn.b, self.a*rhn.b+self.b*rhn.a)
    def __div__(self, rhl):
        sr, si, ol, oi=self.a, self.b, rnl.a, rnl.b 
        r = float(ol**2 + oi**2)
        return Complex((sr*ol+si*oi)/r, (si*ol-sr*oi)/r)
    def __abs__(self):
        return sqrt(self.a**2 + self.b**2)

    
l=Complex(1,9)
k=Complex(2,5)
c=l+k
c1=l-k
c2=l*k
print(c)
print(c1)
print(c2)
