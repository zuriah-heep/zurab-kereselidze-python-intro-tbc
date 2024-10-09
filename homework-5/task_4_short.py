n = int(input('Enter a natural number below 50: '))

if not 0 < n < 50:
    print('Entered number does not meet the requirement.')
    exit(1)

print(' ' * (n - 1) + '*')

for i in range(1, n):
    print(' ' * (n - i - 1), '/' * i, '|', '\\' * i, sep = '')

print(' ' * (n - 1) + '|')