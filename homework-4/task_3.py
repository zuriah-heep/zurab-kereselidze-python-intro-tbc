n = int(input('Enter a whole number n such that 0 < n < 1000: '))

if not 0 < n < 1000:
    print('Entered number is not between 0 and 1000.')
    exit(1)

for i in range(1, n + 1):
    if not n % i:
        print(i, end = ' ')