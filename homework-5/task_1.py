n = int(input('Enter a natural number below 50: '))

if not 0 < n < 50:
    print('Entered number does not meet the requirement.')
    exit(1)

for i in range(1, n + 1):
    amount = 0
    print(i, '–', end = ' ')
    for j in range(1, i + 1):
        if not i % j:
            amount += 1
            if amount > 3:
                break
            print(j, end = ' ')
    print()