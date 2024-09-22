from random import randint
n = int(input('Enter a whole number n so that 0 < n < 30: '))

if not 0 < n < 30:
    print('Entered number is not between 0 and 30.')
    exit(1)

max_n = 0
for i in range(n):
    random_number = randint(0, 1000)
    if random_number > max_n:
        max_n = random_number

print(max_n)