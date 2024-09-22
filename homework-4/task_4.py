n = int(input('Enter a natural number below 20: '))

if not 0 <= n < 20:
    print('Entered number does not meet the requirement.')
    exit(1)

if n <= 1:
    print(n)
else:
    prev1 = 1
    prev2 = 0
    for i in range(2, n + 1):
        number = prev1 + prev2
        prev2 = prev1
        prev1 = number
    print(number)