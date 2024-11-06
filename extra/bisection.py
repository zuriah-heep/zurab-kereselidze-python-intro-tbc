from turtle import Screen, Turtle

cube = 27
epsilon = 0.0001

low = 0
low0 = low
high = max(1, cube)
high0 = high

answer = (low + high) / 2

width = 1600
height = 700

length = int(width / 2) - 100
y = int(height / 2) + 30

def axis(y, color):
    t.color(color)
    t.up()
    t.goto(-length - 30, y)
    t.down()
    t.forward(2 * (length + 30))
    t.up()
    t.goto(length + 20, y - 5)
    t.down()
    t.goto(length + 30, y)
    t.goto(length + 20, y + 5)
    t.up()

def tick(x, y, low, high, color):
    coordinate = -length + int((x - low) * 2 * length / (high - low))
    t.color(color)
    t.up()
    t.goto(coordinate, y + 10)
    t.down()
    t.goto(coordinate, y - 10)
    t.up()
    t.goto(coordinate, y - 30)
    t.write(str(x), align="center", font=("Arial", 12, "normal"))

screen = Screen()
screen.setup(width = width, height = height)
t = Turtle()
t.width(3)
iterations = 0
while abs(answer ** 3 - cube) >= epsilon:
    if iterations % 3 == 0:
        y -= 80
        axis(y, 'black')
        low0 = low
        high0 = high
        tick(high, y, low0, high0, 'blue')
        tick(low, y, low0, high0, 'red')

    if abs(answer ** 3) > abs(cube):
        high = answer
        tick(high, y, low0, high0, 'blue')
    else:
        low = answer
        tick(low, y, low0, high0, 'red')

    answer = (low + high) / 2
    iterations += 1

tick(low, y, low0, high0, 'green')

print(f"Number of iterations = {iterations}")
print(f"Answer = {answer}")

t.hideturtle()
screen.mainloop()