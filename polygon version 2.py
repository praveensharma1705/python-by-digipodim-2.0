from turtle  import *

speed('fastest')


def polygon(sides, length, color, width):
    pencolor(color)
    pensize(width)
    for i in range(sides):
        forward(length)
        right(360/sides)

# calling
polygon(4, 100, 'red' , 5)  # square
goto(200, 0)
polygon(6, 50, 'green' , 2) # hexagon
goto(200,200)
polygon(3, 100, 'blue' , 10) #triangle
polygon(4, 200, 'yellow' ,6) # rectangle
goto(300, 200)

hideturtle()
mainloop()
