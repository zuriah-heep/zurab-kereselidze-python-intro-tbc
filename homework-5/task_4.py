n = int(input('Enter a natural number below 50: '))

if not 0 < n < 50:
    print('Entered number does not meet the requirement.')
    exit(1)

for i in range(1, n):
    print(' ', end = '')
print('*')

for i in range(1, n):
    for j in range(1, n + i + 1):
        if j < n - i:
            print(' ', end='')
        elif j < n:
            print('/', end='')
        elif j > n:
            print('\\', end='')
        else:
            print('|', end='')
    print()

for i in range(1, n):
    print(' ', end = '')
print('|')