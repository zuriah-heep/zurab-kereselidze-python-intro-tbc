import math

a = float(input("Enter side a length of a triangle: "))
b = float(input("Enter side b length of a triangle: "))
c = float(input("Enter side c length of a triangle: "))

p = a + b + c
s = p/2
h = s * (s - a) * (s - b) * (s - c)

if h > 0:
    area = math.sqrt(h)
    print("The perimeter of the triangle is", p)
    print("The area of the triangle is", area)
else:
    print("A triangle with such side lengths does not exist.")
