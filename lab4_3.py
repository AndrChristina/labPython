#Python. Лабораторна робота № 4.3. Андріїшин Христина, FI-9119
print('Python. Лабораторна робота № 4.3')
print('Андріїшин Христина, FI-9119')
from math import*
a=float(input('a = '))
x=float(input('x = '))
n=0
while abs(x**2-a)>10**(-4):
	x=(1/2)*(x + a / x) 
	n+=1
print('sqrt(a) =', float(x))
