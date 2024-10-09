n = int(input('Enter a non-negative whole number below 20: '))

if not 0 <= n < 20:
    print('Entered number does not meet the requirement.')
    exit(1)

print(0, end = ' ')

if n > 0:
    print(1, end = ' ')

if n > 1:
    index = 2
    prev1 = 1
    prev2 = 0
    while index <= n:
        index += 1
        number = prev1 + prev2
        prev2 = prev1
        prev1 = number
        print(number, end = ' ')