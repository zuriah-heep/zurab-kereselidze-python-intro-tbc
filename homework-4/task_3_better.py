from math import floor, sqrt

n = int(input('Enter a whole number n such that 0 < n < 1000: '))

if not 0 < n < 1000:
    print('Entered number is not between 0 and 1000.')
    exit(1)

divisors = []

for i in range(1, floor(sqrt(n)) + 1):
    if not n % i:
        divisors.append(i)
        divisors.append(int(n/i))

print(*sorted(set(divisors)))