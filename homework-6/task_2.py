n = int(input('Enter a natural number up to 1000: '))

if not 0 < n <= 1000:
    print('Entered number does not meet the requirement.')
    exit(1)

print(n, end = '')

while n - 1:
    if n % 2:
        n = 3 * n + 1
    else:
        n = int(n / 2)
    print(' ->', n, end = '')