#Python. Лабораторна робота № matplotlib. Андріїшин Христина, FI-9119
print('Python. Лабораторна робота № matplotlib')
print('Андріїшин Христина, FI-9119')
from numpy import*
import matplotlib.pyplot as plt
import math
def y(x):
    return x*sin(5*x)
x=linspace(-2,5,250)
plt.plot(x,y(x),label='x*sin(5*x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('grafic.png',dpi=200)
plt.show()
