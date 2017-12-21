from turtle import *

setup(500, 500)
title("Turtle Keys")

def k1():
    forward(10)

def k2():
    left(45)

def k3():
    right(45)

def k4():
    backward(10)

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

listen()
mainloop()
