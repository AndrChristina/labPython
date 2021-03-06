from math import*
from tkinter import*

root = Tk()
root.title('Андріїшин Христина')
root.geometry('500x500')

label=Label(root, text='Побудова графіку', font='Arial 14 bold', bg='green')
label.pack(fill=X)

canvas = Canvas(root, height=360, width = 480, bg='#F5DEB3')
canvas.pack()

x0, y0 = 200, 300
x1 =50; x2 = 350; dx=10
canvas.create_line(0, y0,470, y0, fill = 'green', arrow = LAST)
canvas.create_line(x0, 10,x0, 350, fill = 'green', arrow = FIRST)

canvas.create_text(225,310, text='25')
canvas.create_text(300,310, text='100')
canvas.create_text(x0+5,10, text='y', anchor=W)
canvas.create_text(450,300, text='x', anchor = NW)

p = 50
while p<=350:
    canvas.create_line(p, 295,p, 305, fill = 'green')
    canvas.create_line(195, p, 205, p, fill = 'green')
    p+=25
points=[]
for x in range(x1,x2+dx,dx):
    y = y0-(x-x0)**2/100
    z = (x,y)
    points.append(z)
    
print(points)
print(len(points))
canvas.create_line(points, fill='blue', smooth=1, width=2)
button = Button(root, text='Закрити', command = quit)
button.pack()
root.mainloop()
