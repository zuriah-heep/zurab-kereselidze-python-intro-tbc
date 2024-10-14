n = int(input('Enter a natural number below 10: '))

if not 0 < n < 10:
    print('Entered number does not meet the requirement.')
    exit(1)

i = 0
while i <= n:
    j = 0
    while j <= n + i:
        if j < n - i:
            print(' ', end=' ')
        else:
            print(abs(n - j), end=' ')
        j += 1
    print()
    i += 1