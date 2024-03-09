import turtle
import time
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple'])

start = time.time()

def draw_circle(size,angle,shift):
    global start
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    end = time.time()
    elapsed = end-start

    if (elapsed > 180):
        size = 30
        angle = 0
        shift = 1
        start = time.time()
        turtle.reset()
        turtle.pensize(4)
        turtle.hideturtle
    draw_circle(size + 5, angle +1, shift+1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
turtle.hideturtle()
draw_circle(30,0,1)
