from math import*
def  f(x,b):
  k = 2
  second = (pow(-1,0)*pow(x,2*0+1))/factorial(2*0+1)
  yield second
  first = (pow(-1,1)*pow(x,2*1+1))/factorial(2*1+1)
  a = abs(second - first)
  while (a > b):
    yield first
    k += 1
    second = first
    first = (pow(-1,k)*pow(x,2*k+1))/factorial(2*k+1)
    a = abs(second - first)
  yield first
sp = [x for x in f(5,0.1)]
suma = 0
for x in sp: suma += x
print(sp)
print('Сума = ', suma)
