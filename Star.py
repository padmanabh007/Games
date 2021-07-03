from turtle import *

title('Star')
speed(1)
bgcolor('Black')
pencolor('blue')
pensize(2)
setup (width=1000, height=1000, startx=0, starty=0)

def small_star() :
    left(30)
    backward(30)
    left(30)
    forward(60)
    right(120)
    forward(60)
    left(30)
    backward(70)
    left(30)
    forward(61.5)
    left(30)
    backward(40)

left(30)
backward(300)
small_star()
forward(600)
small_star()
right(150)
forward(600)
small_star()
left(180)
forward(700)
small_star()
backward(615)
small_star()
forward(410)
hideturtle()

mainloop()