from turtle import *

width(3)
up()
goto(-150, -50)
down()
for i in range(2):
    forward(200)
    left(50)
    forward(200)
    left(180 - 50)

hideturtle()
done()