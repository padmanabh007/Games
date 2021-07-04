from turtle import *
from random import *
from time import *

COLORS=['red','spring green','aquamarine','blue','yellow','pink','green','purple','orange','navy']
def run_race(turtles,d):
    while True:
        for i in turtles:
            i.forward(randrange(5,10))
            x,y=map(int,i.pos())
            if y>=350 :
                sleep(5)
                quit(f"Turtle in colour {d[i].upper()} Win !..")
        

n=int(input('Enter the number of racers (2-10) : '))
if n<2 or n>10 :
    quit("Invalid input try again ")
title('TURTLE RACE')
setup(800, 800)
turtles_n=[]
x=600//n
posx=-300
c=[]
d={}
for i in range(n) :
    t=Turtle()
    t.shape('turtle')
    while True:
        ch=choice(COLORS)
        if ch not in c:
            c.append(ch)
            break
    t.color(ch)
    d[t]=ch
    t.pu()
    t.setpos(posx,-350)
    t.pd()
    t.left(90)
    turtles_n.append(t)
    posx=posx+x
run_race(turtles_n,d)