from random import uniform

number_min = float(input('Input lower limit for generating a random number: '))
number_max = float(input('Input upper limit for generating a random number: '))

random_float = uniform(number_min, number_max)
number_rounded = round(random_float, 1)

print(number_rounded)