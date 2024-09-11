import math

a = float(input("Enter side a length of a triangle: "))
b = float(input("Enter side b length of a triangle: "))
c = float(input("Enter side c length of a triangle: "))

p = a + b + c
s = p/2

if (s - a) * (s - b) * (s - c) > 0:
    # Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The perimeter of the triangle is", p)
    print("The area of the triangle is", area)
else:
    print("A triangle with such side lengths does not exist.")