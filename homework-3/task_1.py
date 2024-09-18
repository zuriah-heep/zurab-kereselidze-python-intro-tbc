x = float(input('Input number x: '))
y = float(input('Input number y: '))

z = x**y

if int(x) == x:
    x = int(x)
if int(y) == y:
    y = int(y)
if int(x) == x:
    z = int(z)

print(x, '^', y, '=', z)