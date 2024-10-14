n = int(input('Enter a natural number below 10: '))

if not 0 < n < 10:
    print('Entered number does not meet the requirement.')
    exit(1)

i = 0
while i <= n:
    i += 1
    j = 1
    while j < i:
        print(j, end=' ')
        j += 1
    print()

while i > 2:
    i -= 1
    j = 1
    while j < i:
        print(j, end=' ')
        j += 1
    print()