import math
from random import random
from turtle import *

n = int(input('Enter a natural number greater than 1: '))

if n <= 1:
    print('Entered number does not meet the requirement.')
    exit(1)

screen = Screen()
t = Turtle()
t.width(3)

t.penup()
t.goto(-200, -200)
t.pendown()

t.forward(400)

t.penup()
t.goto(190, -205)
t.pendown()
t.goto(200, -200)
t.goto(190, -195)

t.penup()
t.goto(-200, -200)
t.setheading(90)
t.pendown()

t.forward(400)

t.penup()
t.goto(-205, 190)
t.pendown()
t.goto(-200, 200)
t.goto(-195, 190)

for i in range(n):
    a = random()
    b = random()
    t.penup()
    t.goto(a * 360 - 200, b * 360 - 200)
    t.pendown()
    if math.sqrt(a ** 2 + b ** 2) <= 1:
        t.dot(6, "red")
    else:
        t.dot(6, "green")

t.hideturtle()
screen.mainloop()
