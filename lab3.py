#Python. Лабораторна робота № 3. Андріїшин Христина, FI-9119
print('Python. Лабораторна робота № 3')
print('Андріїшин Христина, FI-9119')
from math import*
print('Введіть значення:')
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
if not(sin(2*a)) or not(atan(b)):
    print('Значення змінних виходять за область визначення функції')
else:
    f=(sin(2*a)/(a-3))+(atan(b)/c)
    print('f =',f)
