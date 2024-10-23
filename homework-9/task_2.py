import math
from random import random

n = int(input('Enter a natural number greater than 1: '))

if n <= 1:
    print('Entered number does not meet the requirement.')
    exit(1)

counter = 0
for i in range(n):
    a = random()
    b = random()
    if math.sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1

pi = 4 * counter / n
print(pi)

"""
აქაც ვიღებთ π-ს.
აქ ვიღებთ 1x1 კვარდატს და 1 რადიუსის მქონე წრის მეოთხედ სექტორს რომელიც კვარდატში თავსდება.
counter ითვლის კვადრატში შემთხვევითად დასმული წერტილების რა რაოდენობა მოხვდება წრის სექტორში.
counter / n არის ალბათობა იმისა რომ წერტილი მოხვდება სექტორში. მეორე მხრივ იგივე ალბათობა ტოლია სექტორის ფართობი
გაყოფილი კვადრატის ფართობზე.
ანუ counter / n = (π * 1^2 / 4) / 1^2 = π/4, საიდანაც π = 4 * counter / n
"""