from random import randint

number = randint(1, 100)
count = 0

while count < 10:
    n = int(input('Enter a whole number between 0 and 100: '))

    if not 0 <= n <= 100:
        print('Entered number does not meet the requirement.')
        continue

    if n > number:
        print('high')
    elif n < number:
        print('low')
    else:
        print('You are winner')
        break

    count += 1

if count == 10:
    print('Computer is winner')