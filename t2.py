from turtle import *

pencolor('yellow')
pensize(2)
bgcolor('black')

for i in range(5):
    fd(100)
    rt(360/5)
    for i in range (5):
        fd(50)
        rt(360/5)

        hideturtle()
        mainloop