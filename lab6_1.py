#Python. Лабораторна робота № 6.1. Андріїшин Христина, FI-9119
print('Python. Лабораторна робота № 6.1.')
print('Андріїшин Христина, FI-9119')
x=list(input('List: '))
print(x)
m=0
for i in range(1,len(x)-1):
    if int(x[i-1])<int(x[i]) and int(x[i])>int(x[i+1]):
        m += 1
print(m)

