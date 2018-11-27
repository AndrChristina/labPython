#Python. Лабораторна робота № 4.1. Андріїшин Христина, FI-9119
print('Python. Лабораторна робота № 4.1')
print('Андріїшин Христина, FI-9119')
from math import*
n=1
s=0
a=((-1)**(n-1))/n**n
while a>=10**(-4):
    a=((-1)**(n-1))/n**n
    s+=a
    n+=1
print('s =', s)
print('a_n =',  round(a,4))
print('Кількість ітерацій  =', n)
